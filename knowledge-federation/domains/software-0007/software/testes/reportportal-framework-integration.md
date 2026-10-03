---
id: software.testes.tranche19.001334
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://reportportal.io/docs/log-data-in-reportportal/test-framework-integration/Python/pytest/", "https://github.com/reportportal/reportportal"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ReportPortal: integrar com o framework de testes

## Em uma frase
Cada framework possui agente que envia os resultados automaticamente, configurado por arquivo de projeto e identificação do lançamento.

## Por que importa
Automatizar o envio elimina etapas manuais e mantém o painel atualizado a cada execução da suíte.

## Como funciona
Configure o agente no projeto, defina endereço, projeto e chave, e marque os testes com os metadados desejados.

## Exemplo
Marcações do framework podem virar atributos automaticamente, classificando os casos sem código adicional de integração.

## Limites e trade-offs
Envio configurado por engano para o projeto errado mistura dados entre times, e chaves de acesso versionadas expõem a credencial de integração.

## Como verificar
Execute a suíte com a integração ativa e confirme que o lançamento aparece com a contagem de casos correta.

## Conexões
- [[reportportal-attachments-and-logs]] — Veja também: ReportPortal: registrar evidências no item.
- [[reportportal-modes-and-projects]] — Veja também: ReportPortal: separar modos de execução e projetos.

## Fontes
- [ReportPortal — Integração com pytest](https://reportportal.io/docs/log-data-in-reportportal/test-framework-integration/Python/pytest/) — configuração do agente e marcação de testes; consultado em 2026-10-03.
- [ReportPortal — repositório oficial](https://github.com/reportportal/reportportal) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
