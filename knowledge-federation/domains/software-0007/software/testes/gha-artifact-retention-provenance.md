---
id: software.testes.tranche08.000225
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://docs.github.com/en/actions/tutorials/store-and-share-data", "https://docs.github.com/en/actions/reference/security/secure-use"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GitHub Actions: reter artifacts sem perder proveniência

## Em uma frase
Anexe artifacts de teste ao run e defina retenção compatível com auditoria, privacidade e custo.

## Por que importa
Relatórios e evidências ajudam a diagnosticar falhas, mas podem conter segredos ou dados pessoais e não devem permanecer indefinidamente.

## Como funciona
Nomeie artefato com contexto de execução, limite conteúdo, controle quem baixa e configure retenção explícita conforme política organizacional.

## Exemplo
Relatório JUnit e screenshot são publicados com commit e job; arquivo de ambiente ou credencial fica fora do artifact.

## Limites e trade-offs
Artifact não é backup permanente nem prova de integridade por si só; políticas de expiração e permissões podem variar por configuração do repositório.

## Como verificar
Baixe artifact de run autorizado, confirme associação ao commit, teste expiração e procure segredos ou dados que não deveriam ser armazenados.

## Conexões
- [[gha-job-output-untrusted-artifacts]] — Veja também: GitHub Actions: não confiar em artifacts de execução não privilegiada.
- [[docker-build-secrets-nao-arg-env]] — Veja também: Docker: não inserir secrets em ARG, ENV ou layers.

## Fontes
- [GitHub Actions — Store and share data](https://docs.github.com/en/actions/tutorials/store-and-share-data) — upload, download e retenção de artifacts; consultado em 2026-10-02.
- [GitHub Actions — Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) — least privilege, secrets, script injection e revisão de logs; consultado em 2026-10-02.
