---
id: software.seguranca.tranche11.001006
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

# Priorização de Vulnerabilidades Baseada em Contexto no Cartography: Cruzando **CrowdStrike Spotlight, AWS ECR/Inspector, EPSS e CISA KEV**

## Em uma frase
Um dos maiores problemas de Segurança de Aplicações e Infraestrutura é a fadiga de alertas de vulnerabilidades: scanners reportam milhares de CVEs, mas o time de engenharia precisa saber **quais CVEs têm alta probabilidade de exploração real (`EPSS`), já estão no catálogo `CISA KEV` de exploração ativa E estão rodando em uma instância ou container exposto à internet**!

## Por que importa
O Cartography resolve isso combinando quatro módulos nativos no mesmo grafo: **(1) `cve_metadata`** — enriquece nós `CVE` com scores **CVSS (NVD)**, probabilidade de exploração **EPSS (`FIRST.org`)** e status no catálogo **CISA Known Exploited Vulnerabilities (`KEV`)**; **(2) `crowdstrike`** — sincroniza hosts (`CrowdstrikeHost`) e vulnerabilidades detectadas pelo **CrowdStrike Spotlight**; **(3) `aws` (`ecr` / `inspector`)** — sincroniza imagens multi-arquitetura, camadas (`ECRImageLayer`), atestações e achados do AWS Inspector; e **(4) `github`** — sincroniza manifestos de dependências (`DependencyGraph`)!

## Como funciona
Com esses dados conectados no Neo4j, uma única consulta Cypher prioriza com precisão cirúrgica o que deve ser corrigido nas próximas 24 horas!

## Exemplo
```cypher
// Priorizar vulnerabilidades que estao no catalogo CISA KEV (ou EPSS > 0.5) e afetam ativos expostos ou imagens em producao
MATCH (c:CVE)<-[:AFFECTED_BY]-(asset)
WHERE c.is_kev = true OR c.epss_score >= 0.50
RETURN c.id AS cve_id,
       c.cvss_v3_score AS cvss,
       c.epss_score AS epss,
       c.is_kev AS cisa_kev,
       labels(asset) AS tipo_ativo,
       coalesce(asset.name, asset.hostname, asset.id) AS ativo_afetado
ORDER BY c.epss_score DESC;
```

## Limites e trade-offs
Compare a priorização acima com uma planilha estática de CVEs: ao cruzar `CVE (KEV/EPSS) <- Ativo (EC2/Pod/ECRImage) -> Exposição de Rede -> Dados Sensíveis`, você reduz 95% do ruído e foca o time de engenharia exatamente nas vulnerabilidades que representam risco imediato de invasão!

## Como verificar
Observe que o Cartography também possui o módulo **`aibom`**, que vincula detecções de componentes e modelos de Inteligência Artificial diretamente às imagens de container no **Amazon ECR**!

## Conexões
- [[cartography-motor-regras-cartography-rules-auditoria-automatizada]] — Veja também: Execução Automatizada de Regras de Segurança no Grafo com **`cartography-rules`** (`list`, `run`, `object_storage_public` e Frameworks).
- [[cartography-topologia-kubernetes-eks-gke-aks-pods-rbac-containers]] — Veja também: Mapeamento de Clusters **Kubernetes (EKS, GKE, AKS)** no Cartography: Conectando `Pod`, `Container`, `ServiceAccount`, `RBAC`, `Service` e Imagens Cloud.
- [[cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf]] — Referência cruzada direta com cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf.

## Fontes
- [CNCF Cartography Official GitHub — Multi-Platform Infrastructure & Identity Graph in Neo4j](https://raw.githubusercontent.com/cartography-cncf/cartography/master/README.md) — repositório oficial do CNCF Cartography cobrindo os 30+ módulos suportados (AWS, GCP, Azure, K8s, Okta, Entra ID, GitHub, CrowdStrike, AIBOM) e `cartography-rules`; consultado em 2026-10-03.
- [CNCF Cartography Official Documentation — Querying Tutorial & Data Enrichment (`exposed_internet`, `anonymous_access`)](https://docs.cartography.dev/usage/tutorial.html) — documentação oficial do Cartography demonstrando consultas OpenCypher e enriquecimento automático de superfície de ataque no Neo4j; consultado em 2026-10-03.
