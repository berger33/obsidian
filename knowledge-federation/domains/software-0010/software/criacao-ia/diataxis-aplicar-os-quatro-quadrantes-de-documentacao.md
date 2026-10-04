---
id: software.criacao_ia.tranche02.000191
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md"
fontes: ["https://diataxis.fr/explanation/", "https://diataxis.fr/how-to-guides/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Framework Diátaxis: estruturar documentação técnica em quatro quadrantes

## Em uma frase
O framework Diátaxis classifica a documentação técnica em quatro modos complementares: Tutoriais, Guias How-To, Referência e Explicação.

## Por que importa
Misturar instrução inicial com detalhes exaustivos de API confunde iniciantes e frustra engenheiros experientes que buscam respostas rápidas.

## Como funciona
Separe seus documentos conforme a intenção do leitor: Tutoriais para aprendizagem prática orientada a novatos; How-To para solução de problemas de trabalho; Referência para descrições técnicas de arquitetura; e Explicação para compreensão teórica e trade-offs.

## Exemplo
```text
// Os Quatro Quadrantes do Framework Diataxis
         │ Pratica           │ Teoria
─────────┼───────────────────┼────────────────────
Estudo   │ 1. Tutoriais      │ 4. Explicacao
Trabalho │ 2. Guias How-To   │ 3. Referencia
```

## Limites e trade-offs
Tentar cobrir múltiplos quadrantes em uma única página gera textos desorganizados e de difícil manutenção ao longo das versões do software.

## Como verificar
Inspecione o índice da documentação e confirme que os artigos estão distribuídos coerentemente nas quatro pastas correspondentes.

## Conexões
- [[diataxis-construir-tutoriais-focados-no-primeiro-sucesso]] — Veja também: Diátaxis Tutoriais: conduzir novos usuários ao primeiro resultado palpável.
- [[diataxis-redigir-guias-how-to-para-tarefas-de-producao]] — Conexão temática direta com diataxis-redigir-guias-how-to-para-tarefas-de-producao.
- [[documentacao-escolher-entre-tutorial-e-referencia]] — Conexão temática direta com documentacao-escolher-entre-tutorial-e-referencia.

## Fontes
- [Diátaxis Documentation Framework — Explanation](https://diataxis.fr/explanation/) — Especificação formal do quadrante de explicação, arquitetura conceitual e análise de trade-offs. Consulta: 2026-10-04.
- [Diátaxis Documentation Framework — How-to Guides](https://diataxis.fr/how-to-guides/) — Guia para redação de passos orientados a problemas práticos de produção e trabalho diário. Consulta: 2026-10-04.
