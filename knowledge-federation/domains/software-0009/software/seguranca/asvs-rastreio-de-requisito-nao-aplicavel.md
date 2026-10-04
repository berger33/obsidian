---
id: software.seguranca.tranche17.001699
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://owasp.org/projects/asvs", "https://github.com/OWASP/ASVS"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OWASP ASVS: Rastreio de requisito não aplicável

## Em uma frase
**OWASP ASVS — Rastreio de requisito não aplicável:** Exclusões precisam de justificativa e escopo para evitar confundir falta de teste com ausência de risco.

## Por que importa
O recorte de **rastreio de requisito não aplicável** ajuda a definir critérios verificáveis para desenho, implementação, testes e aquisição de aplicações. A equipe registra risco, evidência e responsável.

## Como funciona
Para **rastreio de requisito não aplicável**, requisitos identificados por versão e código são associados a evidências de projeto e testados no nível de rigor escolhido. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Marque requisito de componente inexistente como não aplicável e cite arquitetura aprovada que sustenta a decisão. Teste em staging autorizado.

## Limites e trade-offs
Mudança arquitetural pode invalidar a justificativa antiga. Exceções exigem responsável e prazo.

## Como verificar
Revise exclusões a cada mudança relevante e procure requisito sem status ou evidência. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[asvs-uso-do-padrao-em-aquisicao-de-software]] — Complementa o tópico com owasp asvs: uso do padrão em aquisição de software.

## Fontes
- [OWASP Application Security Verification Standard](https://owasp.org/projects/asvs) — página oficial do ASVS, objetivos, versão estável e orientação de identificadores versionados; consultado em 2026-10-04.
- [OWASP ASVS — Repository](https://github.com/OWASP/ASVS) — repositório oficial com requisitos versionados e histórico do projeto; consultado em 2026-10-04.
