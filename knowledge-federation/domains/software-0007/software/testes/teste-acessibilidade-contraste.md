---
id: software.testes.tranche07.000114
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
fontes: ["https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html", "https://www.w3.org/TR/WCAG22/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de contraste de texto e componentes", "Teste: Teste de contraste de texto e componentes"]
lote: software-testes-2000-0001
---

# Teste de contraste de texto e componentes

## Em uma frase
Meça contraste nas cores efetivamente renderizadas em cada estado relevante e confronte os resultados com o critério WCAG aplicável.

## Por que importa
Texto ou controle difícil de distinguir pode impedir leitura e operação, particularmente para pessoas com baixa visão ou em condições de visualização desfavoráveis.

## Como funciona
Verifique combinação foreground/background em texto normal e grande e examine indicadores e componentes não textuais conforme seus critérios próprios. Teste estados hover, foco, desabilitado e erro; não use cor sozinha para comunicar significado.

## Exemplo
Para um botão de pagamento, meça texto e limite visual nas variantes normal, foco e erro, incluindo sobreposição de imagem ou tema escuro; confirme que o conteúdo continua distinguível sem depender da cor do alerta.

## Limites e trade-offs
Ferramentas podem estimar cores erradas quando há transparência, gradiente, imagem ou composição dinâmica. As exceções da WCAG devem ser justificadas pelo contexto e não presumidas.

## Como verificar
Registre valores e pares de cor com ferramenta apropriada, verifique a renderização real e faça uma inspeção visual; selecione limiar segundo tamanho e categoria do conteúdo, não uma regra única.

## Conexões
- [[teste-acessibilidade-foco-visivel-ordem]] — aprofundamento relacionado.
- [[teste-acessibilidade-regressao-multimodal]] — aprofundamento relacionado.

## Fontes
- [W3C WAI — Understanding Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — limiares de contraste para texto; consultado em 2026-10-01.
- [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/) — critérios testáveis de acessibilidade para conteúdo web; consultado em 2026-10-01.
