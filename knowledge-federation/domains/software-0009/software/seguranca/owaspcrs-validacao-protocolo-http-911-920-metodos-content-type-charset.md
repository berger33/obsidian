---
id: software.seguranca.tranche02.000118
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
fontes: ["https://coreruleset.org/docs/2-how-crs-works/2-1-anomaly_scoring/", "https://raw.githubusercontent.com/coreruleset/coreruleset/main/README.md", "https://github.com/coreruleset/coreruleset"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OWASP CRS Políticas de Protocolo HTTP (`900200–900250` e `REQUEST-911`/`920`): restrição de métodos HTTP, `Content-Type` e versões TLS/HTTP

## Em uma frase
No arquivo `crs-setup.conf` (regras `900200` a `900250`), o usuário parametriza as políticas estritas de protocolo aplicadas pelos arquivos **`REQUEST-911-METHOD-ENFORCEMENT.conf`** e **`REQUEST-920-PROTOCOL-ENFORCEMENT.conf`**, incluindo a lista de **métodos HTTP permitidos (`tx.allowed_methods`)**, **`Content-Type` permitidos (`tx.allowed_request_content_type`)**, versões HTTP e extensões/cabeçalhos restritos.

## Por que importa
Por padrão no CRS, `tx.allowed_methods` permite apenas `GET HEAD POST OPTIONS`; se a sua API REST legítima utiliza `PUT`, `PATCH` e `DELETE` e você não descomentar e ajustar a regra `900200`, toda chamada `PUT` ou `DELETE` será bloqueada pela regra **`911100` (*Method is not allowed by policy*)**!

## Como funciona
Configurando explicitamente a regra `900200` em `crs-setup.conf` (ou escopada por rota em `BEFORE-CRS`) para incluir `GET HEAD POST OPTIONS PUT PATCH DELETE`, você alinha a política de protocolo ao contrato OpenAPI da sua API.

## Exemplo
```apache
# Regra 900200 no crs-setup.conf liberando PUT, PATCH e DELETE para APIs RESTful:
SecAction \
    "id:900200,\
    phase:1,\
    nolog,\
    pass,\
    t:none,\
    setvar:'tx.allowed_methods=GET HEAD POST OPTIONS PUT PATCH DELETE'"
```

## Limites e trade-offs
Da mesma forma, se sua API utiliza um `Content-Type` customizado (como `application/vnd.api+json` ou `application/grpc`), adicione-o em `tx.allowed_request_content_type` (regra `900220`) para evitar falsos positivos na regra `920420`.

## Como verificar
Teste chamadas `PATCH` e `DELETE` contra a API protegida e confirme que a regra `911100` não é acionada.

## Conexões
- [[owaspcrs-exclusion-packages-pre-construidos-wordpress-nextcloud-dokuwiki]] — Veja também: OWASP CRS Rule Exclusion Packages e CRS v4 Plugins: perfis oficiais de exclusão para WordPress, Nextcloud, Drupal e cPanel.
- [[owaspcrs-inspecao-outbound-response-950-a-959-prevencao-vazamento-dados]] — Veja também: OWASP CRS Inspeção de Resposta Outbound (`RESPONSE-950` a `959`): bloqueio de vazamento de erros SQL, stack traces e web shells.

## Fontes
- [OWASP Core Rule SetOfficial Documentation — Anomaly Scoring Mode (Inbound/Outbound Scores, Thresholds, Severity Points & Collaborative Detection)](https://coreruleset.org/docs/2-how-crs-works/2-1-anomaly_scoring/) — Documentação oficial do OWASP CRS explicando o mecanismo de pontuação de anomalias (Inbound/Outbound), pesos por severidade (CRITICAL=5, ERROR=4, WARNING=3, NOTICE=2) e avaliação nas regras 949110 e 959100; consultado em 2026-10-03.
- [OWASP Core Rule Set GitHub — README.md (CRS v4 Architecture, Attack Categories, Paranoia Levels & False Positive Handling)](https://raw.githubusercontent.com/coreruleset/coreruleset/main/README.md) — README oficial do coreruleset/coreruleset apresentando a arquitetura do OWASP CRS v4, cobertura de ataques e integração com motores WAF; consultado em 2026-10-03.
- [OWASP Core Rule Set (CRS) — Official GitHub Repository](https://github.com/coreruleset/coreruleset) — Repositório oficial Apache-2.0 do OWASP Core Rule Set; consultado em 2026-10-03.
