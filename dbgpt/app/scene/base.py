from enum import Enum
from typing import List


class Scene:
    def __init__(
        self,
        code,
        name,
        describe,
        param_types: List = [],
        is_inner: bool = False,
        show_disable=False,
        prepare_scene_code: str = None,
    ):
        self.code = code
        self.name = name
        self.describe = describe
        self.param_types = param_types
        self.is_inner = is_inner
        self.show_disable = show_disable
        self.prepare_scene_code = prepare_scene_code


class ChatScene(Enum):
    ChatWithDbExecute = Scene(
        code="chat_with_db_execute",
        name="数据对话",
        describe="通过自然语言与数据进行对话，目前主要是结构化与半结构化数据的对话，可以辅助做数据分析与洞察。 ",
        param_types=["DB Select"],
    )
    ExcelLearning = Scene(
        code="excel_learning",
        name="Excel Learning",
        describe="Analyze and summarize your excel files.",
        is_inner=True,
    )
    ChatExcel = Scene(
        code="chat_excel",
        name="Excel对话",
        describe="通过自然语言对话的方式，实现Excel数据的解读与分析。",
        param_types=["File Select"],
        prepare_scene_code="excel_learning",
    )

    ChatWithDbQA = Scene(
        code="chat_with_db_qa",
        name="数据库对话",
        describe="通过与数据库对话完成数据库性能分析、优化等工作, 当前ChatDB只有一些基础的能力，后面会随着社区的迭代，逐步增强。",
        param_types=["DB Select"],
    )
    ChatExecution = Scene(
        code="chat_execution",
        name="Use Plugin",
        describe="Use tools through dialogue to accomplish your goals.",
        param_types=["Plugin Select"],
    )

    ChatAgent = Scene(
        code="chat_agent",
        name="插件",
        describe="支持基本的插件仓库与插件拓展的能力。 项目内置一个搜索插件。",
        param_types=["Plugin Select"],
    )

    InnerChatDBSummary = Scene(
        "inner_chat_db_summary", "DB Summary", "Db Summary.", True
    )

    ChatNormal = Scene(
        "chat_normal", "Chat Normal", "Native LLM large model AI dialogue."
    )
    ChatDashboard = Scene(
        "chat_dashboard",
        "报表分析",
        "通过自然语言进行智能的报表生成与分析，实现生成式BI(GBI)，说说话就可以把数据看板做出来。",
        ["DB Select"],
    )
    ChatKnowledge = Scene(
        "chat_knowledge",
        "知识库对话",
        "知识库提供了根据私域知识问答的能力，可以根据知识库构建智能问答系统、阅读助手等多种产品，使用RAG的技术，对知识检索进行增强。 ",
        ["Knowledge Space Select"],
    )
    ExtractTriplet = Scene(
        "extract_triplet",
        "Extract Triplet",
        "Extract Triplet",
        ["Extract Select"],
        True,
    )
    ExtractSummary = Scene(
        "extract_summary",
        "Extract Summary",
        "Extract Summary",
        ["Extract Select"],
        True,
    )
    ExtractRefineSummary = Scene(
        "extract_refine_summary",
        "Extract Summary",
        "Extract Summary",
        ["Extract Select"],
        True,
    )
    ExtractEntity = Scene(
        "extract_entity", "Extract Entity", "Extract Entity", ["Extract Select"], True
    )
    QueryRewrite = Scene(
        "query_rewrite", "query_rewrite", "query_rewrite", ["query_rewrite"], True
    )

    @staticmethod
    def of_mode(mode):
        return [x for x in ChatScene if mode == x.value()][0]

    @staticmethod
    def is_valid_mode(mode):
        return any(mode == item.value() for item in ChatScene)

    def value(self):
        return self._value_.code

    def scene_name(self):
        return self._value_.name

    def describe(self):
        return self._value_.describe

    def param_types(self):
        return self._value_.param_types

    def show_disable(self):
        return self._value_.show_disable

    def is_inner(self):
        return self._value_.is_inner
