---
id: software.testes.tranche07.000135
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
fontes: ["https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final", "https://sre.google/sre-book/data-integrity/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Exercício de recuperação com RTO e RPO", "Teste: Exercício de recuperação com RTO e RPO"]
lote: software-testes-2000-0001
---

# Exercício de recuperação com RTO e RPO

## Em uma frase
Meça em exercício controlado se a recuperação atende objetivos declarados de tempo e perda máxima de dados, incluindo dependências necessárias.

## Por que importa
Existência de um plano não comprova que a equipe consegue recuperar no prazo ou no ponto de dados esperado durante uma interrupção real.

## Como funciona
Defina RTO, RPO, cenário, escopo, responsáveis e critérios de segurança. Faça restauração ou failover em ambiente autorizado, calcule tempo até serviço utilizável e distância entre último dado confirmado e ponto recuperado.

## Exemplo
Durante drill trimestral, restaure o serviço a partir de backup marcado e reproduza logs disponíveis; compare tempo de retorno e timestamp do último evento válido com objetivos internos.

## Limites e trade-offs
RTO e RPO são objetivos organizacionais definidos por risco e negócio, não números universais. Exercícios podem afetar produção e precisam de janela, comunicação e plano de abortar.

## Como verificar
Registre evidência temporal, componentes indisponíveis, diferenças de dados e ações corretivas; repita após correção e não declare sucesso somente porque o processo terminou sem erro.

## Conexões
- [[testes-restore-backup-integridade]] — aprofundamento relacionado.
- [[test-planning-objetivos-escopo-comunicacao]] — aprofundamento relacionado.

## Fontes
- [NIST SP 800-34 Rev. 1 — Contingency Planning](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) — planejamento, prioridades e exercício de contingência; consultado em 2026-10-01.
- [Google SRE — Data Integrity](https://sre.google/sre-book/data-integrity/) — recuperação deve ser testada de ponta a ponta e validada continuamente; consultado em 2026-10-01.
