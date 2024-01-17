from mycroft import MycroftSkill, intent_file_handler


class EasyShopping(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    # Adapt 意图处理
    @intent_file_handler('faq.easy_shopping')
    def handle_faq_easy_shopping(self, message):
        self.speak_dialog('faq.easy_shopping')

    @intent_file_handler('faq.easy_shopping_capabilities')
    def handle_faq_easy_shopping_capabilities(self, message):
        self.speak_dialog('faq.easy_shopping_capabilities')

    # Padatious 意图处理
    @intent_handler('faq_easy_shopping')
    def handle_faq_easy_shopping_padatious(self, message):
        self.speak_dialog('faq_easy_shopping')

    @intent_handler('faq_easy_shopping_capabilities')
    def handle_faq_easy_shopping_capabilities_padatious(self, message):
        self.speak_dialog('faq_easy_shopping_capabilities')

def create_skill():
    return EasyShopping()

