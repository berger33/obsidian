---
id: software.testes.tranche12.000630
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://github.com/postmanlabs/newman/blob/develop/README.md", "https://learning.postman.com/docs/postman-cli/postman-cli-installation/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Newman: avaliar o modo de manutenção antes de expandir uso

## Em uma frase
O README atual informa que Newman está em modo de manutenção e recomenda Postman CLI para workflows novos que precisem acompanhar recursos recentes.

## Por que importa
Essa condição muda a decisão entre conservar um job legado estável e investir numa nova automação acoplada a funcionalidades que podem não chegar ao runner.

## Como funciona
Para collections já exportadas, registre a versão do Newman e valide compatibilidade do fluxo existente; para um projeto novo, compare migração com as capacidades mantidas do Postman CLI.

## Exemplo
Uma equipe pode continuar executando collections antigas em CI enquanto cria um spike separado para verificar autenticação, scripts e relatórios no CLI recomendado atualmente.

## Limites e trade-offs
Modo de manutenção não significa que toda execução existente parou de funcionar, e uma troca de ferramenta pode exigir alterações de coleção, credenciais ou pipeline.

## Como verificar
Revise o README da versão instalada e rode uma coleção representativa nos dois fluxos antes de declarar a migração equivalente.

## Conexões
- [[newman-collection-source-version]] — Veja também: Newman: fixar a origem da collection executada.

## Fontes
- [Newman — README e opções](https://github.com/postmanlabs/newman/blob/develop/README.md) — estado de manutenção, CLI, opções, reporters e uso como biblioteca; consultado em 2026-10-02.
- [Postman CLI — instalação e visão geral](https://learning.postman.com/docs/postman-cli/postman-cli-installation/) — instalação e posicionamento do runner de linha de comando recomendado para novos workflows; consultado em 2026-10-02.
