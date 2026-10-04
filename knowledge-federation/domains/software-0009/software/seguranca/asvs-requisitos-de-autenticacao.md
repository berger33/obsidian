---
id: software.seguranca.tranche17.001695
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

# OWASP ASVS: Requisitos de autenticação

## Em uma frase
**OWASP ASVS — Requisitos de autenticação:** Requisitos de autenticação ajudam especificar proteção de credenciais, sessão e recuperação de conta.

## Por que importa
O recorte de **requisitos de autenticação** ajuda a definir critérios verificáveis para desenho, implementação, testes e aquisição de aplicações. A equipe registra risco, evidência e responsável.

## Como funciona
Para **requisitos de autenticação**, requisitos identificados por versão e código são associados a evidências de projeto e testados no nível de rigor escolhido. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Revise fluxo de login e recuperação de senha contra os requisitos aplicáveis antes do lançamento. Teste em staging autorizado.

## Limites e trade-offs
Atender mecanismo isolado não assegura resistência a abuso, phishing ou configuração incorreta do provedor. Exceções exigem responsável e prazo.

## Como verificar
Teste rate limiting, recuperação, expiração e invalidade de sessão com casos registrados. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[asvs-autorizacao-e-controle-de-acesso]] — Complementa o tópico com owasp asvs: autorização e controle de acesso.

## Fontes
- [OWASP Application Security Verification Standard](https://owasp.org/projects/asvs) — página oficial do ASVS, objetivos, versão estável e orientação de identificadores versionados; consultado em 2026-10-04.
- [OWASP ASVS — Repository](https://github.com/OWASP/ASVS) — repositório oficial com requisitos versionados e histórico do projeto; consultado em 2026-10-04.
