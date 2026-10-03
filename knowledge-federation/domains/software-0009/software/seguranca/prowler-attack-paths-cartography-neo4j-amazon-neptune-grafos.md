---
id: software.seguranca.tranche02.000173
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/prowler-cloud/prowler/master/README.md", "https://docs.prowler.com/introduction", "https://github.com/prowler-cloud/prowler"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Prowler `Attack Paths`: análise de caminhos de ataque combinando inventário `Cartography` com achados do Prowler em `Neo4j` ou `Amazon Neptune`

## Em uma frase
Conforme documentado na seção *Attack Paths* do README oficial do Prowler, o **Prowler Local Server / Cloud** estende automaticamente cada varredura AWS concluída construindo um **grafo de caminhos de ataque (*Attack Paths*)** que cruza o inventário estrutural da nuvem coletado pelo **Cartography** com as vulnerabilidades e falhas de configuração detectadas pelo Prowler.

## Por que importa
Olhar achados isolados em uma lista plana não mostra o risco composto: uma instância EC2 com uma falha média exposta na internet que possui uma Instance Profile IAM capaz de assumir uma Role administrativa forma um caminho crítico de comprometimento total da conta!

## Como funciona
O worker da API do Prowler executa a ingestão do Cartography em um banco temporário e persiste o grafo de longo prazo em um de dois backends configuráveis via **`ATTACK_PATHS_SINK_DATABASE`**: **`neo4j`** (padrão já incluído no `docker-compose.yml` na porta Bolt `7687`) ou **`neptune`** (**Amazon Neptune** na porta `8182` autenticado via IAM SigV4).

## Exemplo
```bash
# Variáveis de configuração do sink de grafos Attack Paths no Prowler Server:
export ATTACK_PATHS_SINK_DATABASE="neo4j"
export NEO4J_HOST="neo4j"
export NEO4J_PORT="7687"
```

## Limites e trade-offs
Atenção à nota oficial do README: como a fase de ingestão do Cartography sempre utiliza uma instância Neo4j temporária antes de publicar no sink final, as variáveis `NEO4J_*` devem permanecer configuradas mesmo quando você selecionar `ATTACK_PATHS_SINK_DATABASE=neptune`!

## Como verificar
Verifique no painel de *Attack Paths* da UI do Prowler App os caminhos de escalação de privilégio e exposição pública identificados.

## Conexões
- [[prowler-compliance-frameworks-cis-nist-pci-dss-soc2-iso27001-nis2-ens]] — Veja também: Prowler Frameworks de Conformidade (`--compliance`) e `Prowler ThreatScore`: auditoria automatizada `CIS`, `NIST`, `PCI-DSS`, `SOC2`, `ISO 27001` e `MITRE ATT&CK`.
- [[prowler-selecao-granular-checks-services-severities-categories-regions]] — Veja também: Prowler Filtragem Granular de Execução: `--checks`, `--services`, `--severity`, `--category` e `--region` / `--excluded-checks`.

## Fontes
- [Prowler GitHub — README.md (Open-Source Cloud Security Platform, CLI/Dashboard/Server Architecture, Attack Paths with Cartography/Neo4j & Security Hub)](https://raw.githubusercontent.com/prowler-cloud/prowler/master/README.md) — README oficial do prowler-cloud/prowler documentando a arquitetura da plataforma, execução multi-cloud, configuração de Attack Paths com Neo4j/Amazon Neptune e formatos de saída; consultado em 2026-10-03.
- [Prowler Official Documentation — Introduction & Supported Providers (AWS/Azure/GCP/Kubernetes/SaaS/IaC Coverage, ThreatScore, Compliance & Prowler MCP)](https://docs.prowler.com/introduction) — Documentação oficial de introdução ao Prowler detalhando a matriz de provedores suportados, Prowler ThreatScore, frameworks de conformidade, Mutelist e extensibilidade; consultado em 2026-10-03.
- [Prowler — Official GitHub Repository](https://github.com/prowler-cloud/prowler) — Repositório oficial Apache-2.0 do Prowler; consultado em 2026-10-03.
