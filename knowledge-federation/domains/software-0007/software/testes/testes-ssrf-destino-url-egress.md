---
id: software.testes.tranche07.000126
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-07.md"
fontes: ["https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/19-Testing_for_Server-Side_Request_Forgery", "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste seguro de destinos em funcionalidades de fetch de URL", "Teste: Teste seguro de destinos em funcionalidades de fetch de URL"]
lote: software-testes-2000-0001
---

# Teste seguro de destinos em funcionalidades de fetch de URL

## Em uma frase
Avalie se uma funcionalidade que busca URLs limita destinos e protocolos a uma política explícita, sem alcançar recursos internos não autorizados.

## Por que importa
Servidores frequentemente têm acesso de rede maior que o cliente; uma URL controlada pode atravessar fronteiras de confiança e acessar serviços não expostos publicamente.

## Como funciona
Use um callback externo controlado e ambiente isolado para observar requisições; teste destinos permitidos, bloqueados, redirecionamentos e resolução de nomes conforme política. Não envie requisições para endereços internos reais; valide controles de egress e normalização de URL.

## Exemplo
Para um importador de imagem em staging, forneça a URL de um endpoint de callback próprio e confirme a solicitação esperada; em seguida use destinos reservados de laboratório que a política deve bloquear, sem tocar em metadata ou serviços reais.

## Limites e trade-offs
Resultados cegos podem exigir telemetria de rede e revisão de jobs assíncronos. Resolução DNS, redirects e proxies podem mudar destino; use controles autorizados e nunca infira segurança de ausência de resposta visível.

## Como verificar
Correlacione request ID com logs de egress, registre destino final após redirects e prove que domínios permitidos funcionam enquanto destinos proibidos são recusados sem tentativa de conexão.

## Conexões
- [[risk-based-testing-priorizacao-risco]] — aprofundamento relacionado.
- [[testes-logs-redaction-injection]] — aprofundamento relacionado.

## Fontes
- [OWASP WSTG — Server-Side Request Forgery](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/19-Testing_for_Server-Side_Request_Forgery) — testes controlados de recursos remotos e fronteiras de confiança do servidor; consultado em 2026-10-01.
- [OWASP WSTG — Bypassing Authorization Schema](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema) — testes de autorização horizontal e vertical com contas e permissões distintas; consultado em 2026-10-01.
