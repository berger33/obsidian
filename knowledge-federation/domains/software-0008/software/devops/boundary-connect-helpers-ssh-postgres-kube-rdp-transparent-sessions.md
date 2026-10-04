---
id: software.devops.tranche19.001846
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/hashicorp/boundary/main/README.md", "https://developer.hashicorp.com/boundary/docs/what-is-boundary", "https://github.com/hashicorp/boundary"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# HashiCorp Boundary `boundary connect`: helpers nativos de CLI (`ssh`, `postgres`, `kube`, `http`, `rdp`) e sessões transparentes

## Em uma frase
O subcomando **`boundary connect`** atua como um proxy local na estação do engenheiro que negocia um túnel mTLS autenticado até o Boundary Worker e pode tanto abrir uma porta local efêmera quanto invocar diretamente a ferramenta cliente preferida do usuário (`boundary connect ssh`, `boundary connect postgres`, `boundary connect kube`, `boundary connect rdp`).

## Por que importa
Forçar desenvolvedores e DBAs a abandonar suas ferramentas habituais (`OpenSSH`, `psql`, `DataGrip`, `kubectl`, `Remote Desktop`) para usar apenas um terminal web no navegador reduz a produtividade.

## Como funciona
Quando o engenheiro executa `boundary connect postgres -target-id ttcp_1234567890 -- -d appdb`, a CLI do Boundary autoriza a sessão junto ao Controller, abre um listener TCP em uma porta efêmera em `127.0.0.1` e invoca o binário local `psql` passando o host, a porta local e as credenciais intermediadas automaticamente.

## Exemplo
```bash
# Autenticando via OIDC e conectando diretamente via SSH ou kubectl através do Boundary:
boundary authenticate oidc
boundary connect ssh -target-id ttcp_1234567890 -- -l ubuntu
boundary connect kube -target-id ttcp_9876543210 -- get pods -A
```

## Limites e trade-offs
Ao definir `default_client_port` em um `Target` (ou usar sessões transparentes com o Boundary Desktop / cliente de sistema), a conexão pode usar uma porta local previsível sem precisar copiar portas aleatórias a cada sessão.

## Como verificar
Execute `boundary connect -target-id <id> -listen-port 15432` para abrir apenas o túnel local na porta `15432` e inspecione a sessão ativa com `boundary sessions list`.

## Conexões
- [[boundary-vault-credential-store-brokering-injecao-credenciais-efemeras]] — Veja também: HashiCorp Boundary e HashiCorp Vault: *Credential Brokering* e injeção de credenciais efêmeras por sessão.
- [[boundary-workers-ingress-egress-multi-hop-redes-isoladas-enclaves]] — Veja também: HashiCorp Boundary Workers e Multi-Hop Sessions: encadeamento de Ingress e Egress Workers para redes privadas sem rota de entrada.

## Fontes
- [HashiCorp Boundary GitHub — README.md (Identity-Aware Proxy, Controller & Workers, PostgreSQL & KMS Requirements, Dev Mode & CLI)](https://raw.githubusercontent.com/hashicorp/boundary/main/README.md) — README oficial do hashicorp/boundary detalhando os componentes Controller e Worker, requisitos de banco SQL e KMS, hierarquia de Scopes e boundary connect; consultado em 2026-10-03.
- [HashiCorp Developer — What is Boundary? (Core Workflow, OIDC Authentication, Vault Credential Brokering/Injection, Multi-Hop & Session Recording)](https://developer.hashicorp.com/boundary/docs/what-is-boundary) — Documentação oficial do HashiCorp Boundary cobrindo acesso just-in-time sem agente, credenciais dinâmicas via Vault, sessões transparentes e gravação BSR; consultado em 2026-10-03.
- [HashiCorp Boundary — Official GitHub Repository](https://github.com/hashicorp/boundary) — Repositório oficial do HashiCorp Boundary; consultado em 2026-10-03.
