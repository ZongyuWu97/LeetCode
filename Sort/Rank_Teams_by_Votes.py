class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        nTeams = len(votes[0])
        record = {}
        for vote in votes:
            for i, v in enumerate(vote):
                if not v in record:
                    record[v] = [0] * nTeams + [v]
                record[v][i] -= 1
        return ''.join(sorted(votes[0], key=record.get))

