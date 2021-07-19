# Adapted from https://gist.github.com/scharton/102100f39fa9c8a9b55330a507a5590f
import hashlib
import time

# Data you want to generate the proof of work for
# In Bitcoin this would be the previous block header
data = "gjgd"

def proof_of_work(difficulty_bits):

    # calculate the difficulty target
    target = 2 ** (256-difficulty_bits)

    nonce = 0
    while True:
        data_to_be_hashed = (str(data) + " " + str(nonce)).encode('utf-8')
        hash_result = hashlib.sha256(data_to_be_hashed).hexdigest()

        # check if this is a valid result, below the target
        if int(hash_result, 16) < target:
            print("Success with nonce %d" % nonce)
            print("Proof of work %s" % data_to_be_hashed)
            print("Hash is %s" % hash_result)
            return (hash_result, nonce)
        nonce += 1

if __name__ == '__main__':

    hash_result = ''

    # difficulty from 0 to 40 bits
    test_range = 40
    for difficulty_bits in range(0, test_range):

        difficulty = 2 ** difficulty_bits
        print("Difficulty: %ld (%d bits)" % (difficulty, difficulty_bits))

        print("Starting search...")

        # checkpoint the current time
        start_time = time.time()

        # find a valid nonce for the data
        (hash_result, nonce) = proof_of_work(difficulty_bits)

        # checkpoint how long it took to find a result
        end_time = time.time()

        elapsed_time = end_time - start_time
        print("Elapsed Time: %.4f seconds" % elapsed_time)

        if elapsed_time > 0:

            # estimate the hashes per second
            hash_power = float(int(nonce)/elapsed_time)
            print("Hashing Power: %ld hashes per second" % hash_power)

        print()
