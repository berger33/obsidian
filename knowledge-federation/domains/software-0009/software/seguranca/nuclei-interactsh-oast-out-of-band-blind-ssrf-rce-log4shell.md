---
id: software.seguranca.tranche01.000056
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
fontes: ["https://raw.githubusercontent.com/projectdiscovery/nuclei/main/README.md", "https://docs.projectdiscovery.io/opensource/nuclei/overview", "https://github.com/projectdiscovery/nuclei"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Nuclei OAST com `Interactsh` (`{{interactsh-url}}`): detecção *Out-of-Band* sem falsos positivos para Blind SSRF, XXE e RCE

## Em uma frase
O Nuclei possui integração nativa com o **[Interactsh](https://github.com/projectdiscovery/interactsh)** (*Out-of-Band Application Security Testing — OAST*) por meio do placeholder dinâmico **`{{interactsh-url}}`**, permitindo detectar vulnerabilidades cegas (*Blind SSRF*, *Blind XXE*, *Blind RCE*, *Log4Shell*) que não retornam nenhuma diferença visível na resposta HTTP imediata.

## Por que importa
Em uma vulnerabilidade *Blind SSRF* ou *Log4Shell*, o servidor web responde com um `200 OK` normal, mas um worker assíncrono em background faz uma resolução DNS ou requisição HTTP para o endereço injetado no payload.

## Como funciona
Quando um template usa `{{interactsh-url}}` em um header ou parâmetro, o Nuclei gera um subdomínio correlacionado único com chaves criptográficas efêmeras e verifica nos matchers (`part: interactsh_protocol`, `words: ["dns", "http"]`) se o servidor alvo realizou um callback DNS, HTTP ou SMTP para aquele identificador exclusivo.

## Exemplo
```yaml
id: blind-ssrf-header-check

info:
  name: Blind SSRF via X-Forwarded-Host OAST
  author: sec-team
  severity: high
  tags: ssrf,oast

http:
  - method: GET
    path:
      - "{{BaseURL}}/"
    headers:
      X-Forwarded-Host: "{{interactsh-url}}"
    matchers:
      - type: word
        part: interactsh_protocol
        words:
          - "http"
          - "dns"
```

## Limites e trade-offs
Em ambientes corporativos restritos onde callbacks não devem passar por servidores OAST públicos na internet, aponte o Nuclei para o seu próprio servidor `interactsh-server` interno usando a flag **`-iserver`** (`-interactsh-server`) e **`-itoken`**, ou desative OAST com **`-ni`** (`-no-interactsh`).

## Como verificar
Teste a conectividade com o servidor Interactsh executando um template OAST com `-v` ou desative-o com `-ni` em scans puramente locais.

## Conexões
- [[nuclei-workflows-multi-step-flow-engine-variaveis-dinamicas]] — Veja também: Nuclei Workflows e `flow:` Engine: orquestração condicional multi-step e encadeamento de variáveis entre requisições.
- [[nuclei-authenticated-scans-secrets-file-headers-variables-ci-cd]] — Veja também: Nuclei Varreduras Autenticadas (`-H`, `-var` e arquivo de `secrets` com `pre-condition`): autenticação dinâmica em APIs e aplicações.

## Fontes
- [ProjectDiscovery Nuclei GitHub — README.md (YAML Template Engine, Multi-Protocol Support, Filtering Flags, Rate Limiting & CI/CD Reporting)](https://raw.githubusercontent.com/projectdiscovery/nuclei/main/README.md) — README oficial do projectdiscovery/nuclei documentando instalação, flags de filtragem de templates, controle de concorrência, OAST Interactsh e formatos de saída; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Nuclei Overview (Template Anatomy, Matchers/Extractors, Request Clustering, Workflows & Authenticated Scans)](https://docs.projectdiscovery.io/opensource/nuclei/overview) — Visão geral oficial da documentação do Nuclei explicando a anatomia dos templates YAML, agrupamento de requisições, fluxos multi-step e varreduras autenticadas; consultado em 2026-10-03.
- [ProjectDiscovery Nuclei — Official GitHub Repository](https://github.com/projectdiscovery/nuclei) — Repositório oficial MIT do ProjectDiscovery Nuclei; consultado em 2026-10-03.
