---
id: software.seguranca.tranche01.000057
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://docs.projectdiscovery.io/opensource/nuclei/overview", "https://raw.githubusercontent.com/projectdiscovery/nuclei/main/README.md", "https://github.com/projectdiscovery/nuclei"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Nuclei Varreduras Autenticadas (`-H`, `-var` e arquivo de `secrets` com `pre-condition`): autenticação dinâmica em APIs e aplicações

## Em uma frase
Conforme a documentação oficial de *Authenticated Scans* do Nuclei, você pode autenticar varreduras tanto de forma estática — injetando cabeçalhos customizados (`-H "Authorization: Bearer ..."`) ou variáveis de template (`-V` / `-var`) — quanto de forma dinâmica por meio de um arquivo YAML de **`secrets` (`-sf` / `-secret-file`)** com suporte a *Dynamic Fetching* (`pre-condition` que faz login antes da varredura para obter o token/cookie atualizado).

## Por que importa
Passar um token estático na CLI funciona para testes curtos, mas em varreduras longas ou onde cada domínio alvo exige um fluxo de login diferente para obter um cookie de sessão ou token OAuth2, o arquivo `-sf` automatiza a obtenção da credencial.

## Como funciona
O arquivo passado em `-sf secrets.yaml` declara os domínios (`domains:`), o tipo de segredo (`header`, `cookie`, `basic-auth`, `bearer-token`) ou um template de login prévio que extrai o token dinamicamente e o injeta apenas nas requisições destinadas àqueles domínios!

## Exemplo
```bash
# Passando um header de autenticação customizado ou um arquivo de secrets (-sf) na execução:
nuclei -u https://api-staging.example.com \
  -H "Authorization: Bearer ${STAGING_API_TOKEN}" \
  -t ./api-security-templates/
```

## Limites e trade-offs
Nunca inclua tokens reais dentro de templates YAML compartilhados; utilize variáveis `-V token=...` ou o arquivo `-sf` lendo variáveis de ambiente do cofre de CI.

## Como verificar
Use a flag `-debug` (em ambiente local seguro) para inspecionar os cabeçalhos HTTP exatos enviados pelo Nuclei ao alvo.

## Conexões
- [[nuclei-interactsh-oast-out-of-band-blind-ssrf-rce-log4shell]] — Veja também: Nuclei OAST com `Interactsh` (`{{interactsh-url}}`): detecção *Out-of-Band* sem falsos positivos para Blind SSRF, XXE e RCE.
- [[nuclei-controle-taxa-concorrencia-rate-limit-bulk-size-request-clustering]] — Veja também: Nuclei Performance, *Request Clustering* e Rate Limiting (`-rl`, `-c`, `-bs`): proteção do alvo e otimização de tráfego.

## Fontes
- [ProjectDiscovery Nuclei GitHub — README.md (YAML Template Engine, Multi-Protocol Support, Filtering Flags, Rate Limiting & CI/CD Reporting)](https://docs.projectdiscovery.io/opensource/nuclei/overview) — README oficial do projectdiscovery/nuclei documentando instalação, flags de filtragem de templates, controle de concorrência, OAST Interactsh e formatos de saída; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Nuclei Overview (Template Anatomy, Matchers/Extractors, Request Clustering, Workflows & Authenticated Scans)](https://raw.githubusercontent.com/projectdiscovery/nuclei/main/README.md) — Visão geral oficial da documentação do Nuclei explicando a anatomia dos templates YAML, agrupamento de requisições, fluxos multi-step e varreduras autenticadas; consultado em 2026-10-03.
- [ProjectDiscovery Nuclei — Official GitHub Repository](https://github.com/projectdiscovery/nuclei) — Repositório oficial MIT do ProjectDiscovery Nuclei; consultado em 2026-10-03.
