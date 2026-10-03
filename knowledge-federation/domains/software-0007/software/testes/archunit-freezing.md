---
id: software.testes.tranche19.001343
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://www.archunit.org/userguide/html/000_Index.html", "https://github.com/TNG/ArchUnit"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ArchUnit: congelar violações existentes

## Em uma frase
O congelamento registra as violações atuais em armazenamento próprio e passa a reportar apenas violações novas a cada execução.

## Por que importa
Em bases legadas, o congelamento permite bloquear a piora imediata sem exigir a correção completa do passivo de uma vez.

## Como funciona
Crie o armazenamento em execução deliberada, versione-o, proíba atualizações automáticas e reduza o passivo gradualmente.

## Exemplo
Uma regra pode congelar as violações atuais de dependência e falhar quando um novo acesso proibido for introduzido.

## Limites e trade-offs
Permitir a atualização automática do armazenamento apaga o progresso sem aviso, e o congelamento esquecido perpetua o passivo sem prazo.

## Como verificar
Introduza uma violação nova com o armazenamento congelado e confirme que a execução falha apenas por ela.

## Conexões
- [[archunit-coding-rules]] — Veja também: ArchUnit: aplicar convenções de codificação.
- [[archunit-onion-and-diagrams]] — Veja também: ArchUnit: verificar arquitetura em cebola e diagramas.

## Fontes
- [ArchUnit — User Guide](https://www.archunit.org/userguide/html/000_Index.html) — regras, camadas, fatias, congelamento e verificação por diagrama; consultado em 2026-10-03.
- [ArchUnit — repositório oficial](https://github.com/TNG/ArchUnit) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
