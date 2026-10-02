---
id: software.testes.tranche07.000122
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
fontes: ["https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/07-Testing_Session_Timeout", "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/01-Testing_for_Session_Management_Schema"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de timeout e replay de sessão", "Teste: Teste de timeout e replay de sessão"]
lote: software-testes-2000-0001
---

# Teste de timeout e replay de sessão

## Em uma frase
Verifique se a sessão expira por inatividade conforme a política e se um identificador invalidado não volta a autorizar requisições.

## Por que importa
Sessões persistentes em dispositivos compartilhados podem expor dados; um logout visual que não invalida o token mantém o risco no servidor.

## Como funciona
Crie sessão de teste, registre o token de forma protegida e faça requisições em intervalos antes e depois do limite documentado. Depois do timeout e do logout, repita a chamada autenticada com o token antigo e examine resposta e estado.

## Exemplo
Com timeout configurado para o ambiente de QA, aguarde além do limite sem atividade e tente acessar recurso privado; confirme que a API exige nova autenticação e rejeita replay do identificador encerrado.

## Limites e trade-offs
O timeout apropriado depende do risco, e atividade concorrente pode renovar sessão por política. Não grave tokens reais em relatório nem trate limpeza de cache do browser como substituto de invalidação server-side.

## Como verificar
Teste fronteira temporal, renovação por atividade válida, logout em múltiplas abas e token antigo; registre horários e respostas sem incluir segredo reutilizável.

## Conexões
- [[cookies-seguranca-sessao-http]] — aprofundamento relacionado.
- [[test-data-privacidade-sinteticos]] — aprofundamento relacionado.

## Fontes
- [OWASP WSTG — Session Timeout](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/07-Testing_Session_Timeout) — expiração por inatividade deve ser conferida no servidor; consultado em 2026-10-01.
- [OWASP WSTG — Session Management Schema](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/01-Testing_for_Session_Management_Schema) — análise do ciclo de vida e das propriedades do identificador de sessão; consultado em 2026-10-01.
