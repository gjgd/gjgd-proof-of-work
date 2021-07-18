import hashlib
import time

max_nonce = 2 ** 32  # 4 billion

data = "gjgd"

def proof_of_work(difficulty_bits):

    # calculate the difficulty target
    target = 2 ** (256-difficulty_bits)

    for nonce in range(max_nonce):
        data_to_be_hashed = (str(data) + " " + str(nonce)).encode('utf-8')
        hash_result = hashlib.sha256(data_to_be_hashed).hexdigest()

        # check if this is a valid result, below the target
        if int(hash_result, 16) < target:
            print("Success with nonce %d" % nonce)
            print("Proof of work %s" % data_to_be_hashed)
            print("Hash is %s" % hash_result)
            return (hash_result, nonce)

    print("Failed after %d (max_nonce) tries" % nonce)
    return nonce


if __name__ == '__main__':

    nonce = 0
    hash_result = ''

    # difficulty from 0 to 31 bits
    original_max_range = 32
    test_range = 32
    for difficulty_bits in range(test_range):

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
