class BrowserHistory:

    def __init__(self, homepage: str):
        self.Browser = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        self.Browser = self.Browser[:self.index+1]
        self.Browser.append(url)
        self.index +=1

    def back(self, steps: int) -> str:
        if steps > self.index:
            self.index = 0
            return self.Browser[0]
        self.index -= steps
        return self.Browser[self.index]

    def forward(self, steps: int) -> str:
        if self.index + steps<len(self.Browser):
            self.index += steps
            return self.Browser[self.index]
        self.index = len(self.Browser)-1
        return self.Browser[self.index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)