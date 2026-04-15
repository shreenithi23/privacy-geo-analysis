class QueryLimiter:
    def __init__(self, max_queries=10):
        self.max_queries = max_queries
        self.user_counts = {}

    def allow(self, user_id):
        count = self.user_counts.get(user_id, 0)

        if count >= self.max_queries:
            return False

        self.user_counts[user_id] = count + 1
        return True