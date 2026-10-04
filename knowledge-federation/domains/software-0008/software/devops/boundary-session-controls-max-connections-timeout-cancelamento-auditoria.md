---
id: software.devops.tranche19.001848
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

# HashiCorp Boundary Session Controls: limites de conexões por sessão, `session_max_seconds` e revogação em tempo real

## Em uma frase
Cada `Target` no Boundary impõe controles granulares de sessão — especificamente **`session_connection_limit`** (quantas conexões TCP aquela autorização de sessão permite, como `1` para uso único ou `-1` para ilimitadas) e **`session_max_seconds`** (duração máxima da sessão, padrão 8 horas / `28800` segundos) — além de permitir cancelamento imediato de sessões ativas.

## Por que importa
Em uma VPN tradicional, uma vez conectado o usuário mantém o túnel aberto indefinidamente e não há visibilidade por conexão TCP individual; no Boundary, cada conexão a um Target é autorizada individualmente e encerrada exatamente quando o tempo expira ou quando o administrador cancela a sessão.

## Como funciona
Se um incidente de segurança ocorrer ou uma janela de manutenção terminar, um operador autorizado executa `boundary sessions cancel -id s_1234567890`: o Controller notifica o Worker imediatamente e o socket TCP/SSH ativo é cortado em tempo real.

## Exemplo
```bash
boundary targets update tcp \
  -id ttcp_1234567890 \
  -session-connection-limit 1 \
  -session-max-seconds 3600

boundary sessions list -scope-id p_1234567890
boundary sessions cancel -id s_1234567890
```

## Limites e trade-offs
Para clientes de banco de dados (como DBeaver ou DataGrip) que abrem múltiplas conexões TCP paralelas para carregar metadados de tabelas e executar queries, configure `-session-connection-limit -1` no Target do banco.

## Como verificar
Estabeleça uma conexão via `boundary connect`, liste a sessão ativa com `boundary sessions list` e teste a interrupção imediata do socket com `boundary sessions cancel`.

## Conexões
- [[boundary-workers-ingress-egress-multi-hop-redes-isoladas-enclaves]] — Veja também: HashiCorp Boundary Workers e Multi-Hop Sessions: encadeamento de Ingress e Egress Workers para redes privadas sem rota de entrada.
- [[boundary-session-recording-bsr-storage-buckets-auditoria-ssh]] — Veja também: HashiCorp Boundary Session Recording (BSR): gravação e reprodução criptografada de sessões SSH para conformidade.

## Fontes
- [HashiCorp Boundary GitHub — README.md (Identity-Aware Proxy, Controller & Workers, PostgreSQL & KMS Requirements, Dev Mode & CLI)](https://raw.githubusercontent.com/hashicorp/boundary/main/README.md) — README oficial do hashicorp/boundary detalhando os componentes Controller e Worker, requisitos de banco SQL e KMS, hierarquia de Scopes e boundary connect; consultado em 2026-10-03.
- [HashiCorp Developer — What is Boundary? (Core Workflow, OIDC Authentication, Vault Credential Brokering/Injection, Multi-Hop & Session Recording)](https://developer.hashicorp.com/boundary/docs/what-is-boundary) — Documentação oficial do HashiCorp Boundary cobrindo acesso just-in-time sem agente, credenciais dinâmicas via Vault, sessões transparentes e gravação BSR; consultado em 2026-10-03.
- [HashiCorp Boundary — Official GitHub Repository](https://github.com/hashicorp/boundary) — Repositório oficial do HashiCorp Boundary; consultado em 2026-10-03.
