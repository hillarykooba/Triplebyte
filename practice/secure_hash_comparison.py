'''
While all four answers are legitimate attacks on cryptographic hash functions, this function specifically is most vulnerable to timing attacks. The key observation is that the loop that compares the two strings will loop more times (and take longer) if the two hashes share a common prefix. This allows an attacker to go through the hash from beginning to end, and at each character position try all 256 possible bytes. When they guess the correct byte, the comparison will take slightly longer. They can then go on to the next character position, and in short order they'll have extracted the correct hash.
'''


# The following function seems to work, but it wouldn't pass a security review. Which vulnerability is this code most exposed to?

def secure_hash_comparison(user_submitted_hash, database_hash):
    if len(user_submitted_hash) != len(database_hash):
        return False
    for i in range(len(user_submitted_hash)):
        if user_submitted_hash[i] != database_hash[i]:
          return False
    return True
 
# Answer: Timing attacks on the string comparison
