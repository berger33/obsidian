---
id: software.seguranca.tranche17.001698
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

# OWASP ASVS: Evidência de testes automatizados e manuais

## Em uma frase
**OWASP ASVS — Evidência de testes automatizados e manuais:** Automação ajuda regressão, enquanto casos complexos podem exigir análise manual e revisão contextual.

## Por que importa
O recorte de **evidência de testes automatizados e manuais** ajuda a definir critérios verificáveis para desenho, implementação, testes e aquisição de aplicações. A equipe registra risco, evidência e responsável.

## Como funciona
Para **evidência de testes automatizados e manuais**, requisitos identificados por versão e código são associados a evidências de projeto e testados no nível de rigor escolhido. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Para requisito de autorização, anexe resultado de teste automatizado e nota de revisão de threat model. Teste em staging autorizado.

## Limites e trade-offs
Passar uma suíte não demonstra que todos os cenários aplicáveis foram modelados. Exceções exigem responsável e prazo.

## Como verificar
Verifique versão do teste, ambiente e requisito alvo; avalie lacunas de cobertura. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[asvs-rastreio-de-requisito-nao-aplicavel]] — Complementa o tópico com owasp asvs: rastreio de requisito não aplicável.

## Fontes
- [OWASP Application Security Verification Standard](https://owasp.org/projects/asvs) — página oficial do ASVS, objetivos, versão estável e orientação de identificadores versionados; consultado em 2026-10-04.
- [OWASP ASVS — Repository](https://github.com/OWASP/ASVS) — repositório oficial com requisitos versionados e histórico do projeto; consultado em 2026-10-04.
