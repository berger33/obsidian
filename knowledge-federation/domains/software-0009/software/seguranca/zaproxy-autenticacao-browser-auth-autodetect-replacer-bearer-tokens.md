---
id: software.seguranca.tranche01.000045
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
fontes: ["https://www.zaproxy.org/docs/automate/automation-framework/", "https://raw.githubusercontent.com/zaproxy/zaproxy/main/README.md", "https://github.com/zaproxy/zaproxy"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# ZAP Autenticação no Automation Framework: `browser` auth, `autodetect` de sessão e injeção de tokens com o job `replacer`

## Em uma frase
O ZAP Automation Framework suporta dois caminhos principais para realizar varreduras autenticadas: 1) configurar **`authentication`** no `context` (incluindo **`browser` authentication**, **`client` script authentication** e **`autodetect`** de gerenciamento/verificação de sessão fornecidos pelo add-on *Authentication Helper*); ou 2) injetar um cabeçalho `Authorization: Bearer <JWT>` ou cookie via job **`replacer`**.

## Por que importa
Sem autenticação configurada, qualquer scanner DAST testa apenas a tela de login pública e recebe HTTP `401 Unauthorized` em todas as rotas protegidas onde reside 95% da lógica de negócio da aplicação.

## Como funciona
Para APIs stateless protegidas por JWT ou API Key em pipelines de CI, o job **`replacer`** é o método mais direto e determinístico: ele adiciona ou substitui o cabeçalho `Authorization` em todas as requisições enviadas pelo ZAP ao alvo. Já para aplicações web com login OIDC/MFA/SPA, o modo `browser` authentication com `autodetect` realiza o login real em navegador headless e extrai os tokens/cookies de sessão automaticamente.

## Exemplo
```yaml
jobs:
  - type: replacer
    parameters:
      deleteAllRules: true
    rules:
      - description: "Injeta token JWT de teste nas chamadas de API"
        matchType: "REQ_HEADER"
        matchString: "Authorization"
        replacement: "Bearer ${ZAP_AUTH_TOKEN}"
```

## Limites e trade-offs
Como o Automation Framework interpola variáveis de ambiente no formato `${VAR}`, nunca grave tokens ou senhas em texto claro dentro do YAML versionado: injete `${ZAP_AUTH_TOKEN}` a partir do cofre de segredos do CI.

## Como verificar
Configure uma URL de verificação (`verification.pollUrl`) no contexto para que o ZAP confirme continuamente que as requisições autenticadas estão retornando HTTP `200`.

## Conexões
- [[zaproxy-importacao-schemas-apis-openapi-graphql-soap-postman]] — Veja também: ZAP Segurança de APIs (`openapi`, `graphql`, `soap` e `postman`): importação de contratos para DAST de APIs REST e GraphQL.
- [[zaproxy-passive-scan-config-passive-scan-wait-fila-assincrona]] — Veja também: ZAP `passiveScan-config` e `passiveScan-wait`: ajuste de regras passivas e sincronização obrigatória da fila de análise.

## Fontes
- [OWASP ZAP Official Documentation — Automation Framework (Declarative YAML Plan, env Contexts, Discovery/Scan/Report Jobs & Job Tests)](https://www.zaproxy.org/docs/automate/automation-framework/) — Documentação oficial do Automation Framework do OWASP ZAP detalhando a estrutura YAML env/jobs, substituição dos Packaged Scans e lista completa de jobs suportados; consultado em 2026-10-03.
- [OWASP ZAP GitHub — README.md (Zed Attack Proxy Architecture, Passive & Active Scanners, Container Images & Add-ons)](https://raw.githubusercontent.com/zaproxy/zaproxy/main/README.md) — README oficial do zaproxy/zaproxy apresentando o projeto DAST open-source, modos de execução headless e ecossistema de extensões; consultado em 2026-10-03.
- [OWASP ZAP — Official GitHub Repository](https://github.com/zaproxy/zaproxy) — Repositório oficial Apache-2.0 do OWASP Zed Attack Proxy; consultado em 2026-10-03.
