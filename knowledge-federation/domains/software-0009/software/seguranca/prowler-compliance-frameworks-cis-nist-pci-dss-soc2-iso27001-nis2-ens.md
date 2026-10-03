---
id: software.seguranca.tranche02.000172
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

# Prowler Frameworks de Conformidade (`--compliance`) e `Prowler ThreatScore`: auditoria automatizada `CIS`, `NIST`, `PCI-DSS`, `SOC2`, `ISO 27001` e `MITRE ATT&CK`

## Em uma frase
O Prowler mapeia seus milhares de checks técnicos diretamente para dezenas de padrões regulatórios e de indústria via flag **`--compliance`**, além de calcular o **`Prowler ThreatScore`** (pontuação ponderada de priorização de risco que destaca primeiro as falhas mais críticas).

## Por que importa
Preparar evidências técnicas para auditorias **CIS Benchmarks**, **PCI-DSS v4.0**, **SOC 2**, **ISO/IEC 27001**, **NIST 800-53 / CSF**, **HIPAA**, **GDPR**, **FedRAMP**, **NIS2**, **ENS** ou **MITRE ATT&CK** costumava exigir semanas de coleta manual de screenshots no console da nuvem.

## Como funciona
No Prowler, uma única execução avalia todos os controles técnicos em minutos e gera relatórios específicos por framework de conformidade (em CSV, JSON-OCSF e HTML), mapeando exatamente qual requisito normativo passou (`PASS`) ou falhou (`FAIL`) em cada recurso da conta.

## Exemplo
```bash
# Listando os frameworks de conformidade disponíveis para AWS e executando auditoria CIS + PCI-DSS:
prowler aws --list-compliance
prowler aws --compliance cis_3.0_aws pci_4.0_aws
```

## Limites e trade-offs
Você não precisa rodar o Prowler duas vezes para obter dois relatórios de compliance diferentes: em uma varredura normal (`prowler aws`), o Prowler já gera na subpasta `compliance/` as tabelas de mapeamento para todos os frameworks aplicáveis!

## Como verificar
Inspecione os arquivos gerados em `output/compliance/` após a execução do scan.

## Conexões
- [[prowler-arquitetura-open-cloud-security-platform-cspm-multi-cloud]] — Veja também: Prowler: arquitetura da plataforma open-source de segurança e conformidade multi-cloud (`AWS`, `Azure`, `GCP`, `Kubernetes`, `M365`, `GitHub`).
- [[prowler-attack-paths-cartography-neo4j-amazon-neptune-grafos]] — Veja também: Prowler `Attack Paths`: análise de caminhos de ataque combinando inventário `Cartography` com achados do Prowler em `Neo4j` ou `Amazon Neptune`.

## Fontes
- [Prowler GitHub — README.md (Open-Source Cloud Security Platform, CLI/Dashboard/Server Architecture, Attack Paths with Cartography/Neo4j & Security Hub)](https://raw.githubusercontent.com/prowler-cloud/prowler/master/README.md) — README oficial do prowler-cloud/prowler documentando a arquitetura da plataforma, execução multi-cloud, configuração de Attack Paths com Neo4j/Amazon Neptune e formatos de saída; consultado em 2026-10-03.
- [Prowler Official Documentation — Introduction & Supported Providers (AWS/Azure/GCP/Kubernetes/SaaS/IaC Coverage, ThreatScore, Compliance & Prowler MCP)](https://docs.prowler.com/introduction) — Documentação oficial de introdução ao Prowler detalhando a matriz de provedores suportados, Prowler ThreatScore, frameworks de conformidade, Mutelist e extensibilidade; consultado em 2026-10-03.
- [Prowler — Official GitHub Repository](https://github.com/prowler-cloud/prowler) — Repositório oficial Apache-2.0 do Prowler; consultado em 2026-10-03.
