---
id: software.testes.tranche07.000115
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
fontes: ["https://www.w3.org/WAI/WCAG22/Understanding/reflow.html", "https://www.w3.org/WAI/test-evaluate/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de reflow em zoom e viewport estreito", "Teste: Teste de reflow em zoom e viewport estreito"]
lote: software-testes-2000-0001
---

# Teste de reflow em zoom e viewport estreito

## Em uma frase
Avalie se conteúdo e funcionalidade permanecem disponíveis quando o viewport é estreito ou o usuário amplia o conteúdo, sem exigir rolagem bidimensional indevida.

## Por que importa
Pessoas com baixa visão frequentemente ampliam páginas; layouts que cortam conteúdo ou exigem rolagem horizontal em cada linha aumentam a carga de navegação.

## Como funciona
Teste em viewport equivalente a 320 CSS pixels e com zoom do navegador, percorrendo conteúdo, controles, menus e mensagens. Verifique que texto reflui sem sobreposição, truncamento ou perda de funcionalidade; identifique exceções legítimas, como conteúdo que exige layout bidimensional.

## Exemplo
Abra o fluxo de compra em viewport estreito, aumente o zoom e percorra endereço, resumo e confirmação; confirme que todos continuam utilizáveis sem ocultar ações ou texto essencial.

## Limites e trade-offs
Uma captura estática não prova que interações são usáveis. A exceção para conteúdo que requer layout em duas dimensões é contextual; ela não libera a página inteira de adaptação.

## Como verificar
Use breakpoints de teste definidos pela WCAG, confira conteúdo ao longo do fluxo e registre qualquer scroll horizontal localizado, justificando se a exceção se aplica.

## Conexões
- [[teste-acessibilidade-contraste]] — aprofundamento relacionado.
- [[teste-acessibilidade-regressao-multimodal]] — aprofundamento relacionado.

## Fontes
- [W3C WAI — Understanding Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) — refluxo do conteúdo em viewport estreito e zoom; consultado em 2026-10-01.
- [W3C WAI — Easy Checks and Evaluation](https://www.w3.org/WAI/test-evaluate/) — avaliação combina verificações automáticas e exame manual; consultado em 2026-10-01.
