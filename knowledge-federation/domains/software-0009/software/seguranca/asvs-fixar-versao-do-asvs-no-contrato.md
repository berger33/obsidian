---
id: software.seguranca.tranche17.001691
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

# OWASP ASVS: Fixar versão do ASVS no contrato

## Em uma frase
**OWASP ASVS — Fixar versão do ASVS no contrato:** Requisitos e identificadores podem mudar entre versões, então contrato e plano de teste devem nomear a edição usada.

## Por que importa
O recorte de **fixar versão do asvs no contrato** ajuda a definir critérios verificáveis para desenho, implementação, testes e aquisição de aplicações. A equipe registra risco, evidência e responsável.

## Como funciona
Para **fixar versão do asvs no contrato**, requisitos identificados por versão e código são associados a evidências de projeto e testados no nível de rigor escolhido. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Inclua versão do ASVS no escopo de um assessment de aplicação antes de escolher requisitos. Teste em staging autorizado.

## Limites e trade-offs
Referência sem versão dificulta reproduzir auditoria e comparar resultados ao longo do tempo. Exceções exigem responsável e prazo.

## Como verificar
Confira identificador e texto do requisito no release escolhido e registre a fonte da versão. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[asvs-escolher-nivel-de-verificacao]] — Complementa o tópico com owasp asvs: escolher nível de verificação.

## Fontes
- [OWASP Application Security Verification Standard](https://owasp.org/projects/asvs) — página oficial do ASVS, objetivos, versão estável e orientação de identificadores versionados; consultado em 2026-10-04.
- [OWASP ASVS — Repository](https://github.com/OWASP/ASVS) — repositório oficial com requisitos versionados e histórico do projeto; consultado em 2026-10-04.
