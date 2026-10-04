---
id: software.seguranca.tranche11.001008
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/cartography-cncf/cartography/master/README.md", "https://docs.cartography.dev/usage/tutorial.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Segurança e Governança de **IA em Produção (`AI Security Posture / AIBOM`)** no Cartography: **AWS Bedrock, GCP Vertex AI, OpenAI e Anthropic**

## Em uma frase
Uma das perguntas mais urgentes para CISOs e equipes de Segurança Cloud em 2026 — destacada na própria abertura do `README.md` oficial do Cartography — é: ***"Quais agentes e modelos de Inteligência Artificial estão rodando em produção, quais chaves de API existem e quais permissões de acesso a dados eles possuem?"***

## Por que importa
O Cartography responde a essa pergunta através de cinco módulos dedicados a IA Generativa e MLOps: **(1) AWS Bedrock & SageMaker** (modelos fundacionais, agentes, bases de conhecimento e roles IAM associadas); **(2) GCP Vertex AI**; **(3) `openai`** (organizações, projetos, usuários e chaves de API da OpenAI); **(4) `anthropic`** (`Organization`, `Workspace`, `User`, `ApiKey`); e **(5) `aibom` (*AI Bill of Materials*)** (detecções de bibliotecas, pesos e componentes de IA dentro de imagens de container no **Amazon ECR**)!

## Como funciona
Ao cruzar esses nós no Neo4j, você audita tanto o risco de **Shadow AI** quanto o escopo de permissões IAM concedido a agentes autônomos!

## Exemplo
```cypher
// Auditar usuarios e chaves de API ativas em organizacoes Anthropic e OpenAI e imagens ECR com componentes de IA (AIBOM)
MATCH (org:AnthropicOrganization)-[:RESOURCE]->(key:AnthropicApiKey)
RETURN org.name AS organizacao, key.name AS nome_chave, key.status AS status, key.created_at AS criada_em;
```

## Limites e trade-offs
Por que conectar o **AIBOM** às imagens do **Amazon ECR** e aos Pods do **Kubernetes** no grafo do Cartography é tão poderoso? Porque se uma vulnerabilidade crítica for descoberta em um servidor de inferência ou framework de LLM (como PyTorch, vLLM, LangChain ou LlamaIndex), você localiza em segundos **quais imagens ECR contêm aquele componente de IA e em quais Pods de produção elas estão rodando**!

## Como verificar
Combine essa visibilidade do Cartography com a detecção de chaves `ABSK...` do Amazon Bedrock no **`git-secrets`** e **Gitleaks**.

## Conexões
- [[cartography-topologia-kubernetes-eks-gke-aks-pods-rbac-containers]] — Veja também: Mapeamento de Clusters **Kubernetes (EKS, GKE, AKS)** no Cartography: Conectando `Pod`, `Container`, `ServiceAccount`, `RBAC`, `Service` e Imagens Cloud.
- [[cartography-sincronizacao-multi-conta-update-tag-cleanup-staleness]] — Veja também: Operação em Produção do Cartography: Sincronização Multi-Conta AWS (`--aws-sync-all-profiles`), **`UPDATE_TAG`** e Limpeza de Nós Obsoletos (**`Cleanup Jobs`**).
- [[cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf]] — Referência cruzada direta com cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf.
- [[gitsecrets-registro-padroes-aws-register-aws-bedrock-aws-provider]] — Referência cruzada direta com gitsecrets-registro-padroes-aws-register-aws-bedrock-aws-provider.

## Fontes
- [CNCF Cartography Official GitHub — Multi-Platform Infrastructure & Identity Graph in Neo4j](https://raw.githubusercontent.com/cartography-cncf/cartography/master/README.md) — repositório oficial do CNCF Cartography cobrindo os 30+ módulos suportados (AWS, GCP, Azure, K8s, Okta, Entra ID, GitHub, CrowdStrike, AIBOM) e `cartography-rules`; consultado em 2026-10-03.
- [CNCF Cartography Official Documentation — Querying Tutorial & Data Enrichment (`exposed_internet`, `anonymous_access`)](https://docs.cartography.dev/usage/tutorial.html) — documentação oficial do Cartography demonstrando consultas OpenCypher e enriquecimento automático de superfície de ataque no Neo4j; consultado em 2026-10-03.
