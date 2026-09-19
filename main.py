"""
Main entry point for starting the Ghost Notes Daemon.
"""

import sys
from ghost_notes.daemon import GhostNotesDaemon

def main():
    try:
        daemon = GhostNotesDaemon()
        daemon.start_listeners(block=True)
    except KeyboardInterrupt:
        print("\n[Ghost Notes] Exiting daemon via keyboard interrupt.")
        sys.exit(0)

if __name__ == "__main__":
    main()
