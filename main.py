from guardian import MinorMintGuardian
from integration import MinorMintFintech

def run_minor_mint_agent(item_name, price):
    print(f"\n🔍 [MinorMint Agent] Analyzing: '{item_name}'")
    guardian = MinorMintGuardian()
    fintech = MinorMintFintech()
    is_safe, reason = guardian.analyze_request(item_name)
    if is_safe and 240.0 >= price:
        print(f"🤖 Decision: APPROVED | {reason}")
        fintech.execute_vault_transfer(price)
    else:
        print(f"🤖 Decision: REJECTED | 🚫 {reason}")

if __name__ == "__main__":
    run_minor_mint_agent("Robot Kit", 50.0)
    run_minor_mint_agent("Online Poker", 10.0)
  
