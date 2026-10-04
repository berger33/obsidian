---
id: software.criacao_ia.tranche03.000276
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://playwright.dev/docs/videos", "https://playwright.dev/docs/api/class-browsercontext"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Playwright video: fechar browser context para salvar o arquivo

## Em uma frase
Gravações de vídeo Playwright são finalizadas quando o BrowserContext fecha, não quando o último frame aparece na página.

## Por que importa
Ler caminho ou anexar o arquivo antes do fechamento pode encontrar vídeo ausente ou incompleto. Contextos manuais são comuns em testes de múltiplas páginas e a etapa de cleanup precisa aguardar explicitamente a operação de close.

## Como funciona
Configure `video` como `on`, `retain-on-failure` ou `on-first-retry` conforme custo e objetivo. Playwright Test salva artefatos no diretório de resultados; com `browser.newContext({ recordVideo })`, chame e aguarde `context.close()` antes de consultar `page.video().path()` ou publicar o arquivo. Configure tamanho de viewport de acordo com saída desejada.

## Exemplo
Um cenário multi-page registra vídeo somente na primeira retry. O cleanup fecha todas as pages e aguarda contexto, depois copia vídeo para o reporte apenas se a execução falhou; teste verifica existência e duração do arquivo após close.

## Limites e trade-offs
Vídeo não é disponibilizado enquanto página ou contexto continua aberto. Gravação acrescenta armazenamento e pode capturar conteúdo sensível; tamanho e área capturada variam com viewport e configuração.

## Como verificar
Confirme o arquivo somente após close, teste sucesso e falha para cada modo de retenção e compare dimensões do vídeo com viewport configurada. Verifique que browsers e páginas adicionais pertencem ao contexto esperado.

## Conexões
- [[playwright-trace-retencao-e-dados-de-debug]] — Playwright Trace: coletar diagnóstico sem expor dados de teste.
- [[playwright-expect-poll-e-topass]] — Playwright assertions: escolher expect.poll ou expect.toPass.

## Fontes
- [Playwright — Videos](https://playwright.dev/docs/videos) — define modos de gravação e fechamento do contexto como momento de salvamento Consulta: 2026-10-04.
- [Playwright — BrowserContext API](https://playwright.dev/docs/api/class-browsercontext) — documenta criação, isolamento e fechamento dos contextos que possuem o vídeo Consulta: 2026-10-04.
