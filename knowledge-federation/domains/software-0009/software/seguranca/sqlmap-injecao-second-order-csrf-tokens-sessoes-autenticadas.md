---
id: software.seguranca.tranche05.000404
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/README.md", "https://github.com/sqlmapproject/sqlmap/wiki/Usage", "https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pt-BR.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# sqlmap: Detecção de *Second-Order SQL Injection* (`--second-url`), Renovação de `--csrf-token` e `--eval`

## Em uma frase
O `sqlmap` suporta cenários de estado complexos onde o payload é gravado em uma requisição HTTP inicial, mas a execução vulnerável no banco de dados ocorre em uma segunda URL diferente (`--second-url` / `--second-req`), renovando tokens anti-CSRF (`--csrf-token`) e assinaturas de requisição (`--eval`) a cada tentativa.

## Por que importa
Em *Second-Order SQL Injection*, o endpoint de cadastro armazena o dado no banco, mas uma tela administrativa ou relatório posterior concatena o valor lido do banco em uma nova query SQL sem parametrização.

## Como funciona
Com `--second-url="https://staging.corp/reports/preview"`, o `sqlmap` envia o payload no formulário de entrada e imediatamente busca a resposta de `--second-url` para avaliar o resultado booleano ou erro do SGBD. Se o formulário exige um token CSRF de uso único ou um hash HMAC dos parâmetros, `--csrf-token="authenticity_token"` com `--csrf-url` renova o token e `--eval` executa código Python antes de cada disparo para recalcular assinaturas.

## Exemplo
```bash
# Testar Second-Order SQLi renovando token CSRF automaticamente e avaliando a resposta em outra rota
python3 sqlmap.py -r /tmp/update-profile.http \
  -p display_name \
  --second-url="https://staging.internal.corp/account/audit-preview" \
  --csrf-token="csrf_token" \
  --csrf-url="https://staging.internal.corp/account/edit" \
  --technique=BE --batch
```

## Limites e trade-offs
Se a sessão autenticada expirar por inatividade na aplicação durante os testes, use `--safe-url` e `--safe-freq=20` para manter o cookie de sessão vivo ou `--abort-code=401,403` para interromper imediatamente caso a autenticação caia.

## Como verificar
Configure `--abort-code=401` e verifique nos logs HTTP (`-v 4`) que o `csrf_token` é atualizado antes de cada requisição POST e que a verificação lê o corpo de `--second-url`.

## Conexões
- [[sqlmap-fontes-alvo-request-file-openapi-swagger-burp-logs]] — Veja também: sqlmap: Ingestão de Alvos via Requisição Raw (`-r`), Especificações `--openapi`, Marcadores `*` e Logs de Proxy (`-l`).
- [[sqlmap-tamper-scripts-avaliacao-regras-waf-normalizacao]] — Veja também: sqlmap: Scripts de Transformação (`--tamper`) para Avaliação de Regras de WAF e Normalização de Payloads.
- [[sqlmap-calibracao-level-risk-heuristica-falsos-positivos-comparacao]] — Referência cruzada direta com sqlmap-calibracao-level-risk-heuristica-falsos-positivos-comparacao.
- [[brakeman-prevencao-sql-injection-activerecord-interpolacao-arel]] — Referência cruzada direta com brakeman-prevencao-sql-injection-activerecord-interpolacao-arel.

## Fontes
- [sqlmap Official GitHub — README & Architecture](https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/README.md) — documentação oficial do projeto sqlmap cobrindo arquitetura, instalação e escopo; consultado em 2026-10-03.
- [sqlmap Official Wiki — Usage & Switches Reference](https://github.com/sqlmapproject/sqlmap/wiki/Usage) — manual oficial de opções da CLI, técnicas BEUSTQ, --level, --risk, --tamper e OOB DNS; consultado em 2026-10-03.
- [sqlmap Official Documentation — Portuguese Reference](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pt-BR.md) — referência oficial traduzida do sqlmap; consultado em 2026-10-03.
