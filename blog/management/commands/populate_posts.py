from blog.models import Post
from blog.models import Category
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):
    help= "This commands inserts post data"

    def handle(self, *args, **options):
        
        # Deleting existing data
        Post.objects.all().delete()
        titles = [
            "How Blockchain is Revolutionizing the Finance Industry",
            "The Future of AI: From Automation to AGI",
            "Quantum Computing: The Next Frontier in Computer Science",
            "Decentralized Finance (DeFi): A Beginner's Guide",
            "AI in Healthcare: Opportunities and Ethical Challenges",
            "Understanding the Role of Smart Contracts in Blockchain",
            "Why Data is the New Oil in the Age of AI",
            "Edge Computing vs Cloud Computing: What's the Difference?",
            "Zero-Knowledge Proofs Explained with Simple Examples",
            "Top 10 Use Cases of Blockchain in the Real World",
            "The Rise of Generative AI: Tools, Trends, and Impact",
            "Cybersecurity in the Age of Decentralization",
            "What is Explainable AI (XAI) and Why Does it Matter?",
            "How NLP is Transforming Finance, Law, and Education",
            "Web3 Explained: Beyond Cryptocurrencies and NFTs",
            "Ethics in Artificial Intelligence: Who Sets the Rules?",
            "How AI is Powering Fraud Detection in Banking",
            "The Role of Blockchain in Supply Chain Transparency",
            "Machine Learning vs Deep Learning: Key Differences",
            "What is the Metaverse and Why Are Tech Giants Betting on It?"
        ]

        content = [
            "How Blockchain is Revolutionizing the Finance Industry - Explores how blockchain enhances transparency, security, and efficiency in financial systems.",
            "The Future of AI: From Automation to AGI - A look at how AI is evolving from narrow applications to artificial general intelligence (AGI).",
            "Quantum Computing: The Next Frontier in Computer Science - Introduces quantum computing and its potential to solve problems beyond classical computers.",
            "Decentralized Finance (DeFi): A Beginner's Guide - An introduction to DeFi, a blockchain-based alternative to traditional banking systems.",
            "AI in Healthcare: Opportunities and Ethical Challenges - Covers the benefits and ethical concerns of applying AI in medical diagnosis and treatment.",
            "Understanding the Role of Smart Contracts in Blockchain - Explains how smart contracts automate and enforce agreements without intermediaries.",
            "Why Data is the New Oil in the Age of AI - Discusses the central role of data in powering modern AI systems and innovations.",
            "Edge Computing vs Cloud Computing: What's the Difference? - Compares edge and cloud computing models in terms of latency, control, and use cases.",
            "Zero-Knowledge Proofs Explained with Simple Examples - Breaks down how zero-knowledge proofs allow verification without revealing data.",
            "Top 10 Use Cases of Blockchain in the Real World - Lists practical applications of blockchain in industries like finance, logistics, and voting.",
            "The Rise of Generative AI: Tools, Trends, and Impact - Looks at the growth of generative AI models like ChatGPT and their real-world applications.",
            "Cybersecurity in the Age of Decentralization - Examines security risks and solutions in decentralized systems like blockchain.",
            "What is Explainable AI (XAI) and Why Does it Matter? - Defines XAI and its importance in making AI models more transparent and trustworthy.",
            "How NLP is Transforming Finance, Law, and Education - Shows how natural language processing is streamlining tasks in multiple industries.",
            "Web3 Explained: Beyond Cryptocurrencies and NFTs - Introduces Web3 as a decentralized internet built on blockchain technology.",
            "Ethics in Artificial Intelligence: Who Sets the Rules? - Explores who defines ethical boundaries in the development and use of AI systems.",
            "How AI is Powering Fraud Detection in Banking - Describes how machine learning models are used to detect and prevent financial fraud.",
            "The Role of Blockchain in Supply Chain Transparency - Explains how blockchain helps track goods and improve accountability in supply chains.",
            "Machine Learning vs Deep Learning: Key Differences - Clarifies the difference between ML and DL in terms of complexity and application.",
            "What is the Metaverse and Why Are Tech Giants Betting on It? - Introduces the concept of the metaverse and its potential for immersive digital experiences."
        ]

        img_url = [
    "https://picsum.photos/id/1/800/400",
    "https://picsum.photos/id/2/800/400",
    "https://picsum.photos/id/3/800/400",
    "https://picsum.photos/id/4/800/400",
    "https://picsum.photos/id/5/800/400",
    "https://picsum.photos/id/6/800/400",
    "https://picsum.photos/id/7/800/400",
    "https://picsum.photos/id/8/800/400",
    "https://picsum.photos/id/9/800/400",
    "https://picsum.photos/id/10/800/400",
    "https://picsum.photos/id/11/800/400",
    "https://picsum.photos/id/12/800/400",
    "https://picsum.photos/id/13/800/400",
    "https://picsum.photos/id/14/800/400",
    "https://picsum.photos/id/15/800/400",
    "https://picsum.photos/id/16/800/400",
    "https://picsum.photos/id/17/800/400",
    "https://picsum.photos/id/18/800/400",
    "https://picsum.photos/id/19/800/400",
    "https://picsum.photos/id/20/800/400"
]
        
        categories = Category.objects.all()
        for title, content, img_url in zip(titles, content, img_url):
            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting data"))

