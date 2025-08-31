from database import get_lawyers_by_specialization

def recommend_lawyer():
    specialization = input("🔎 Which type of lawyer do you need? (e.g., Criminal Law, Family Law): ")
    lawyers = get_lawyers_by_specialization(specialization)

    if lawyers:
        print(f"\n✅ Found {len(lawyers)} lawyer(s) for '{specialization}':\n")
        for lawyer in lawyers:
            print(f"👤 {lawyer.name}  |  📞 {lawyer.contact}")
    else:
        print(f"\n❌ Sorry, no lawyers found for specialization: {specialization}")

if __name__ == "__main__":
    recommend_lawyer()
