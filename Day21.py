# Problem : Restore IP Addresses
# Problem Statement : A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []

        def BT(i, address):
            if i == len(s):
                if len(address) == 4:
                    res.append('.'.join(map(str, address)))
                return
            if address[-1] != 0 and address[-1]*10+int(s[i]) <= 255:
                lastItem = address[-1]
                # change the current state to its neighboring state
                address[-1] = lastItem*10+int(s[i])
                BT(i+1, address)  # backtrack(state)
                address[-1] = lastItem  # restore the state (backtrack)

            # The address can not contain more than 4 numbers.
            if len(address) < 4:
                # change the current state to its neighboring state
                address.append(int(s[i]))
                BT(i+1, address)  # backtrack(state)
                address.pop()  # restore the state (backtrack)

        BT(1, [int(s[0])])
        return res
