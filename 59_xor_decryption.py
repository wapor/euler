#!/usr/bin/python

# Each character on a computer is assigned a unique code and the preferred
# standard is ASCII (American Standard Code for Information Interchange). For
# example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes to ASCII,
# then XOR each byte with a given value, taken from a secret key. The advantage
# with the XOR function is that using the same encryption key on the cipher
# text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 =
# 65.

# For unbreakable encryption, the key is the same length as the plain text
# message, and the key is made up of random bytes. The user would keep the
# encrypted message and the encryption key in different locations, and without
# both "halves", it is impossible to decrypt the message.

# Unfortunately, this method is impractical for most users, so the modified
# method is to use a password as a key. If the password is shorter than the
# message, which is likely, the key is repeated cyclically throughout the
# message. The balance for this method is using a sufficiently long password key
# for security, but short enough to be memorable.

# Your task has been made easy, as the encryption key consists of three lower
# case characters. Using cipher1.txt (right click and 'Save Link/Target As...'),
# a file containing the encrypted ASCII codes, and the knowledge that the plain
# text must contain common English words, decrypt the message and find the sum
# of the ASCII values in the original text.


filename = 'cipher1.txt'
cipher = [int(i) for i in open(filename, 'r').read().split(',')]

acceptable = range(ord(' '), ord('~') + 1)  # letters, punctuation and space
letters = range(ord('a'), ord('z'))  # Password is only letters
num_letters = len(letters)
pw_len = 3
pw = range(pw_len)

for pw_idx in xrange(num_letters ** pw_len):  # Iterate over all possible pw indexes.
    for i in range(pw_len):  # Generate pw from its index.
        pw[i] = pw_idx % num_letters + letters[0]
        pw_idx /= num_letters

    # Now decipher the message using this password.
    decipher = []
    j = 0
    for c in cipher:
        d = pw[j] ^ c
        if d not in acceptable:
            break  # Bad character. Try next password.
        decipher.append(d)
        j = (j + 1) % pw_len
    else:
        text = ''.join([chr(j) for j in decipher])
        # I'm pretty sure 'the' and 'and' will appear in the text.
        if 'the' in text.lower() and 'and' in text.lower():
            print text
            print '\nAnswer:', sum(decipher)
            exit()
        
#       0 nul    1 soh    2 stx    3 etx    4 eot    5 enq    6 ack    7 bel
#       8 bs     9 ht    10 nl    11 vt    12 np    13 cr    14 so    15 si
#       16 dle   17 dc1   18 dc2   19 dc3   20 dc4   21 nak   22 syn   23 etb
#       24 can   25 em    26 sub   27 esc   28 fs    29 gs    30 rs    31 us
#       32 sp    33  !    34  "    35  #    36  $    37  %    38  &    39  '
#       40  (    41  )    42  *    43  +    44  ,    45  -    46  .    47  /
#       48  0    49  1    50  2    51  3    52  4    53  5    54  6    55  7
#       56  8    57  9    58  :    59  ;    60  <    61  =    62  >    63  ?
#       64  @    65  A    66  B    67  C    68  D    69  E    70  F    71  G
#       72  H    73  I    74  J    75  K    76  L    77  M    78  N    79  O
#       80  P    81  Q    82  R    83  S    84  T    85  U    86  V    87  W
#       88  X    89  Y    90  Z    91  [    92  \    93  ]    94  ^    95  _
#       96  `    97  a    98  b    99  c   100  d   101  e   102  f   103  g
#      104  h   105  i   106  j   107  k   108  l   109  m   110  n   111  o
#      112  p   113  q   114  r   115  s   116  t   117  u   118  v   119  w
#      120  x   121  y   122  z   123  {   124  |   125  }   126  ~   127 del
