import access_control
import media_engine


SEED_NUM = 6
FAVORITE_ARTIST = "CUP OF JOE"


CONTROL_NUM = max(1, SEED_NUM)

print("CONTROL_NUM:", CONTROL_NUM)
print("FAVORITE ARTIST:", FAVORITE_ARTIST)


# Activity 1
access_level = access_control.compute_access_level(CONTROL_NUM, FAVORITE_ARTIST)

decision = access_control.validate_access(access_level, CONTROL_NUM)

print("Access Level:", access_level)
print("Decision:", decision)


# Activity 2
print("\nSignal Shutdown Simulation")

power = CONTROL_NUM + len(FAVORITE_ARTIST)

calls = media_engine.signal_shutdown(power)

print("Total Recursive Calls:", calls)


# Activity 3
print("\nStreaming Play Counts")

limit = CONTROL_NUM + len(FAVORITE_ARTIST)

stream = media_engine.play_count_stream(limit)

total = 0
records = 0

for value in stream:
    print("Generated:", value)
    total += value
    records += 1


print("Total Plays:", total)
print("Records Processed:", records)