class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        for i in self.categories:
            if i.id == category_id:
                i.name = new_name
                break

    def edit_document(self, document_id, new_file_name):
        for i in self.documents:
            if i.id == document_id:
                i.file_name = new_file_name
                break

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        for i in self.topics:
            if i.id == topic_id:
                i.topic = new_topic
                i.storage_folder = new_storage_folder
                break

    def delete_category(self, category_id):
        for i in self.categories:
            if i.id == category_id:
                self.categories.remove(i)
                break

    def delete_topic(self, topic_id):
        for i in self.topics:
            if i.id == topic_id:
                self.topics.remove(i)
                break

    def delete_document(self, document_id):
        for i in self.documents:
            if i.id == document_id:
                self.documents.remove(i)
                break

    def get_document(self, document_id):
        for i in self.documents:
            if i.id == document_id:
                return i

    def __repr__(self):
        res = ''
        for i in self.documents:
            res += repr(i) + '\n'
        return res[0: len(res) - 1]
