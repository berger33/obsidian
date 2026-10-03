---
id: software.seguranca.tranche11.001017
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
fontes: ["https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md", "https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Redução de Falsos Positivos e Enriquecimento de Rede no Scout Suite: Arquivos de Exceção (**`--exceptions`**) e Mapeamento de CIDRs Conhecidos (**`--ip-ranges`**)

## Em uma frase
Em qualquer auditoria real de nuvem, existem recursos que disparam regras genéricas mas são intencionais e aprovados pela arquitetura de segurança: por exemplo, um bucket S3 específico de CDN que deve ser público, ou regras de Security Group que liberam a porta `22`/`443` não para a internet inteira, mas para os **blocos de IP públicos dos escritórios corporativos, VPNs ou parceiros (`--ip-ranges`)**!

## Por que importa
O Scout Suite resolve ambos os cenários nativamente: primeiro, através da flag **`--ip-ranges <arquivo1.json> <arquivo2.json>`** (com `--ip-ranges-name-key name`), você fornece arquivos JSON mapeando os blocos CIDR conhecidos da sua empresa; durante o pós-processamento, o Scout Suite **substitui e anota automaticamente esses IPs nos relatórios de Security Groups e Network ACLs** com o nome legível do escritório/parceiro!

## Como funciona
Segundo, através da interface web do próprio relatório HTML (ou editando um arquivo JSON), você marca os falsos positivos validados, exporta o arquivo `exceptions.json` e o aplica via **`--exceptions exceptions.json`** (`RuleExceptions`), fazendo com que esses itens deixem de inflar a contagem de riscos em execuções futuras!

## Exemplo
```json
[
  {
    "ip_prefix": "198.51.100.0/24",
    "name": "VPN-Corporativa-Matriz-SP",
    "environment": "Production"
  },
  {
    "ip_prefix": "203.0.113.0/25",
    "name": "Gateway-Parceiro-Pagamentos",
    "environment": "PCI-Scope"
  }
]
```

## Limites e trade-offs
Para usar o arquivo de CIDRs acima (`cidrs-corporativos.json`) junto com seu arquivo de exceções na linha de comando, basta executar: `scout aws --profile auditoria --ip-ranges cidrs-corporativos.json --ip-ranges-name-key name --exceptions exceptions.json --no-browser`.

## Como verificar
Versione tanto o `cidrs-corporativos.json` quanto o `exceptions.json` no repositório Git da equipe de Segurança para manter rastreabilidade de quem aprovou cada exceção.

## Conexões
- [[scoutsuite-reexecucao-offline-fetch-local-update-comparacao-diffs]] — Veja também: Workflow Avançado do Scout Suite: Reavaliação Instantânea com **`--fetch-local`**, Atualização Parcial (**`--update`**) e Exportação JSON/SQLite (`--result-format`).
- [[scoutsuite-auditoria-alibaba-oci-digitalocean-kubernetes-multicloud]] — Veja também: Auditoria de Nuvens Alternativas e Clusters com Scout Suite: **Alibaba Cloud (`aliyun`), Oracle Cloud (`oci`), DigitalOcean (`do`) e Kubernetes (`k8s`)**.
- [[scoutsuite-arquitetura-auditoria-multi-cloud-offline-nccgroup]] — Referência cruzada direta com scoutsuite-arquitetura-auditoria-multi-cloud-offline-nccgroup.

## Fontes
- [NCC Group Scout Suite Official GitHub — Multi-Cloud Security Auditing Tool](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md) — repositório oficial do Scout Suite cobrindo auditoria point-in-time offline para AWS, Azure, GCP, Alibaba Cloud, OCI, DigitalOcean e Kubernetes; consultado em 2026-10-03.
- [Scout Suite Official CLI & Engine Implementation (`ScoutSuite/__main__.py`)](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py) — implementação oficial dos provedores, parâmetros de autenticação, `--fetch-local`, `--update`, `--ruleset`, `--exceptions` e `--ip-ranges`; consultado em 2026-10-03.
