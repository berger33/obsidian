---
id: software.seguranca.tranche02.000107
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
fontes: ["https://raw.githubusercontent.com/corazawaf/coraza/main/README.md", "https://www.coraza.io/docs/seclang/directives/", "https://github.com/corazawaf/coraza"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Coraza em Modo `FIPS 140-3` (`GODEBUG=fips140=on`): detecção em tempo de execução e restrição automática de `t:md5` e `t:sha1`

## Em uma frase
Conforme a seção *FIPS mode* do README oficial do Coraza, o WAF suporta execução sob o **modo FIPS 140-3 nativo do Go** (`GODEBUG=fips140=on`, `=debug` ou `=only`), detectando o modo FIPS automaticamente em tempo de execução sem exigir nenhuma build tag especial.

## Por que importa
Em ambientes governamentais (FedRAMP), financeiros e de saúde sujeitos à conformidade FIPS 140-3, algoritmos criptográficos quebrados como MD5 e SHA-1 não podem ser executados pelo processo em hipótese alguma.

## Como funciona
Quando o Coraza detecta que o runtime Go está com FIPS ativo, as transformações SecLang **`t:md5` e `t:sha1` tornam-se indisponíveis no parse de regras** (permanecendo registradas apenas para retornar um erro claro e imediato caso uma regra tente utilizá-las), garantindo comportamento idêntico em `fips140=on`, `=debug` e `=only`.

## Exemplo
```bash
# Executando o serviço WAF com o modo FIPS 140-3 do Go habilitado em tempo de execução:
GODEBUG=fips140=on ./waf-proxy --config /etc/coraza/coraza.conf
```

## Limites e trade-offs
Antes de ativar `GODEBUG=fips140=on` em produção, valide todo o seu conjunto de regras customizadas para garantir que nenhuma regra legada referencie `t:md5` ou `t:sha1`.

## Como verificar
Inicie o binário com `GODEBUG=fips140=only` e verifique que o carregamento das regras conclui sem erro de transformação proibida.

## Conexões
- [[coraza-build-tags-otimizacao-memoization-multiphase-rx-prefilter]] — Veja também: Coraza Otimização de Performance e Build Tags: memoização de regex/Aho-Corasick, `WAF.Close()`, `SecRxPreFilter` e `no_regex_multiline`.
- [[coraza-body-processors-json-xml-urlencoded-multipart-inspecao]] — Veja também: Coraza Body Processors (`JSON`, `XML`, `URLENCODED`, `MULTIPART`): parsing estruturado de payloads de APIs modernas na Fase 1 e Fase 2.

## Fontes
- [OWASP Coraza GitHub — README.md (Go Enterprise-Grade WAF, ModSecurity SecLang & OWASP CRS v4 Compatibility, Transaction Lifecycle & Integrations)](https://raw.githubusercontent.com/corazawaf/coraza/main/README.md) — README oficial do corazawaf/coraza detalhando a arquitetura do WAF em Go, compatibilidade com SecLang e OWASP CRS v4, extensibilidade e integrações com Caddy, Envoy/Istio, Traefik e HAProxy; consultado em 2026-10-03.
- [OWASP Coraza Official Documentation — SecLang Directives Reference (SecRule, SecAction, SecRuleEngine, Body Access/Limits, Audit Log & Rule Removals)](https://www.coraza.io/docs/seclang/directives/) — Referência oficial das diretivas SecLang implementadas no Coraza WAF, cobrindo controle de motor, limites de body, remoção de regras por ID/Tag e auditoria estruturada; consultado em 2026-10-03.
- [OWASP Coraza WAF — Official GitHub Repository](https://github.com/corazawaf/coraza) — Repositório oficial Apache-2.0 do OWASP Coraza WAF; consultado em 2026-10-03.
