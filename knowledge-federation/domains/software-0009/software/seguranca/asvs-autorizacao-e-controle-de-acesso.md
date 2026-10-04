---
id: software.seguranca.tranche17.001696
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

# OWASP ASVS: Autorização e controle de acesso

## Em uma frase
**OWASP ASVS — Autorização e controle de acesso:** Controles de autorização devem ser avaliados para cada objeto e ação, não apenas para páginas de interface.

## Por que importa
O recorte de **autorização e controle de acesso** ajuda a definir critérios verificáveis para desenho, implementação, testes e aquisição de aplicações. A equipe registra risco, evidência e responsável.

## Como funciona
Para **autorização e controle de acesso**, requisitos identificados por versão e código são associados a evidências de projeto e testados no nível de rigor escolhido. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use duas identidades de papéis diferentes para testar acesso a objeto de outra conta em staging. Teste em staging autorizado.

## Limites e trade-offs
Teste com usuário privilegiado apenas pode mascarar falha de isolamento. Exceções exigem responsável e prazo.

## Como verificar
Inclua casos de objeto horizontal, elevação vertical e negação por padrão. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[asvs-protecao-de-dados-e-criptografia]] — Complementa o tópico com owasp asvs: proteção de dados e criptografia.

## Fontes
- [OWASP Application Security Verification Standard](https://owasp.org/projects/asvs) — página oficial do ASVS, objetivos, versão estável e orientação de identificadores versionados; consultado em 2026-10-04.
- [OWASP ASVS — Repository](https://github.com/OWASP/ASVS) — repositório oficial com requisitos versionados e histórico do projeto; consultado em 2026-10-04.
