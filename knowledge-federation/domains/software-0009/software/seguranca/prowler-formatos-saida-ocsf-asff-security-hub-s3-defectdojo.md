---
id: software.seguranca.tranche02.000178
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

# Prowler Formatos de Saída (`json-ocsf`, `json-asff`, `html`, `csv`) e Integração Nativa com `AWS Security Hub` e `S3`

## Em uma frase
Por meio da flag **`-M` / `--output-modes`** (`csv`, **`json-ocsf`**, **`json-asff`**, `html`), o Prowler exporta todos os achados em padrões abertos de interoperabilidade — com destaque para o **OCSF (*Open Cybersecurity Schema Framework* v1.1.0)** e o **ASFF (*AWS Security Finding Format*)** — além de enviar resultados diretamente para o **AWS Security Hub (`--security-hub`)** e buckets **Amazon S3 (`-B` / `--output-bucket`)**.

## Por que importa
Manter os relatórios do Prowler apenas em arquivos locais na máquina onde o scan rodou impede a correlação centralizada no SIEM, no AWS Security Hub ou no OWASP DefectDojo.

## Como funciona
Ao passar `--security-hub` (ou `--security-hub --send-sh-only-fails` para enviar apenas falhas ou atualizações de achados resolvidos), o Prowler registra e atualiza os achados diretamente no AWS Security Hub de cada região, permitindo acionar regras do Amazon EventBridge para remediação automatizada!

## Exemplo
```bash
# Executando o Prowler gerando saída OCSF + HTML, enviando para o S3 e sincronizando com o AWS Security Hub:
prowler aws \
  --output-modes json-ocsf json-asff html \
  --output-bucket meu-bucket-auditoria-cspm \
  --security-hub \
  --send-sh-only-fails
```

## Limites e trade-offs
Combine a flag `--send-sh-only-fails` com o envio ao Security Hub para economizar custos de ingestão de eventos `PASSED` no AWS Security Hub enquanto ainda arquiva automaticamente achados previamente abertos que foram corrigidos.

## Como verificar
Valide o arquivo `.ocsf.json` gerado na pasta `output/` com `jq '.[0] | {status_code, severity, finding_info}'`.

## Conexões
- [[prowler-saas-github-m365-googleworkspace-okta-iac-containers]] — Veja também: Prowler SaaS, IaC e Containers (`github`, `m365`, `googleworkspace`, `okta`, `iac`, `image`): postura unificada além da IaaS.
- [[prowler-multi-account-aws-organizations-assume-role-azure-subscriptions-gcp]] — Veja também: Prowler Varreduras Multi-Conta em Escala: `AWS AssumeRole` (`-R`), `AWS Organizations` (`-O`), Subscrições Azure e Projetos GCP.

## Fontes
- [Prowler GitHub — README.md (Open-Source Cloud Security Platform, CLI/Dashboard/Server Architecture, Attack Paths with Cartography/Neo4j & Security Hub)](https://raw.githubusercontent.com/prowler-cloud/prowler/master/README.md) — README oficial do prowler-cloud/prowler documentando a arquitetura da plataforma, execução multi-cloud, configuração de Attack Paths com Neo4j/Amazon Neptune e formatos de saída; consultado em 2026-10-03.
- [Prowler Official Documentation — Introduction & Supported Providers (AWS/Azure/GCP/Kubernetes/SaaS/IaC Coverage, ThreatScore, Compliance & Prowler MCP)](https://docs.prowler.com/introduction) — Documentação oficial de introdução ao Prowler detalhando a matriz de provedores suportados, Prowler ThreatScore, frameworks de conformidade, Mutelist e extensibilidade; consultado em 2026-10-03.
- [Prowler — Official GitHub Repository](https://github.com/prowler-cloud/prowler) — Repositório oficial Apache-2.0 do Prowler; consultado em 2026-10-03.
