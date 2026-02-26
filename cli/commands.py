#  Handle what happens after parsing

def handle_explain(args):
    print(f"\nExplaining command: {args.cmd}")
    print(f"Language selected: {args.lang}")
    # later: call explain service
    
def handle_transpile(args):
    print(f"\nTranspiling code: {args.code}")
    print(f"Target language: {args.to}")
    #Later: call transpile service 