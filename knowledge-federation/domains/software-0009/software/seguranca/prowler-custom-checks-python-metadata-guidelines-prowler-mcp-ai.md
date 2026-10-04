---
id: software.seguranca.tranche02.000180
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
fontes: ["https://docs.prowler.com/introduction", "https://raw.githubusercontent.com/prowler-cloud/prowler/master/README.md", "https://github.com/prowler-cloud/prowler"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Prowler Extensibilidade: criação de Checks Customizados (`--checks-folder`), `Check Metadata Guidelines` e servidor `Prowler MCP`

## Em uma frase
Conforme documentado na página *Introduction* (`docs.prowler.com/introduction`), o Prowler permite carregar **Checks Customizados da sua organização (`-x` / `--checks-folder`)** escritos em Python sobre os clientes de serviço já instanciados pelo Prowler, além de oferecer o **`Prowler MCP`** (servidor *Model Context Protocol* que conecta assistentes e agentes de IA ao Prowler Hub e Prowler Cloud/App).

## Por que importa
Toda empresa possui regras internas de governança que vão além dos benchmarks públicos (por exemplo: "todo bucket S3 de produção deve ter a tag `CostCenter` e usar uma chave KMS com prefixo `alias/corp-`").

## Como funciona
No Prowler, cada check é uma pasta contendo dois arquivos simples: `<check_name>.py` (que itera sobre os recursos já coletados em memória pelo serviço, ex.: `s3_client.buckets`, e preenche objetos `Check_Report_AWS` com `status = "PASS"` ou `"FAIL"`) e `<check_name>.metadata.json` (com severidade, descrição, risco e comandos de remediação CLI/Terraform).

## Exemplo
```bash
# Executando checks customizados internos a partir de um diretório local ou bucket S3:
prowler aws --checks-folder ./meus-checks-customizados/
```

## Limites e trade-offs
Como os clientes de serviço do Prowler (ex.: `s3_client`, `iam_client`, `ec2_client`) já buscaram todos os recursos da conta uma única vez na inicialização do serviço, seu check customizado avalia milhares de recursos em memória sem fazer novas chamadas de API à AWS!

## Como verificar
Valide os metadados e a execução do seu check customizado com `prowler aws --checks-folder ./meus-checks-customizados/ -c meu_check_custom`.

## Conexões
- [[prowler-multi-account-aws-organizations-assume-role-azure-subscriptions-gcp]] — Veja também: Prowler Varreduras Multi-Conta em Escala: `AWS AssumeRole` (`-R`), `AWS Organizations` (`-O`), Subscrições Azure e Projetos GCP.

## Fontes
- [Prowler GitHub — README.md (Open-Source Cloud Security Platform, CLI/Dashboard/Server Architecture, Attack Paths with Cartography/Neo4j & Security Hub)](https://docs.prowler.com/introduction) — README oficial do prowler-cloud/prowler documentando a arquitetura da plataforma, execução multi-cloud, configuração de Attack Paths com Neo4j/Amazon Neptune e formatos de saída; consultado em 2026-10-03.
- [Prowler Official Documentation — Introduction & Supported Providers (AWS/Azure/GCP/Kubernetes/SaaS/IaC Coverage, ThreatScore, Compliance & Prowler MCP)](https://raw.githubusercontent.com/prowler-cloud/prowler/master/README.md) — Documentação oficial de introdução ao Prowler detalhando a matriz de provedores suportados, Prowler ThreatScore, frameworks de conformidade, Mutelist e extensibilidade; consultado em 2026-10-03.
- [Prowler — Official GitHub Repository](https://github.com/prowler-cloud/prowler) — Repositório oficial Apache-2.0 do Prowler; consultado em 2026-10-03.
