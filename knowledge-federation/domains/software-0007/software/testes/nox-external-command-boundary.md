---
id: software.testes.tranche14.000828
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://nox.thea.codes/en/stable/config.html", "https://nox.thea.codes/en/stable/tutorial.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Nox: marcar comando externo ao ambiente como exceção

## Em uma frase
`session.run` espera comando disponível no ambiente da sessão; executável do host deve ser autorizado de forma explícita quando necessário.

## Por que importa
A fronteira ajuda a notar ferramentas que escapam do isolamento e podem mudar o resultado entre máquinas.

## Como funciona
Prefira instalar o executável como dependência do ambiente; use opção externa só para ferramenta do host declarada como pré-requisito.

## Exemplo
Uma sessão local pode abrir navegador do sistema com permissão `external=True`, enquanto a suite CI usa driver instalado em ambiente próprio.

## Limites e trade-offs
Autorizar um executável externo não fixa sua versão nem garante que exista no agente remoto.

## Como verificar
Rode em imagem de CI documentada e registre versão da ferramenta externa se ela influenciar resultado.

## Conexões
- [[nox-session-install-run-boundary]] — Veja também: Nox: separar dependências instaladas do executável chamado.
- [[nox-posargs-test-filter-forwarding]] — Veja também: Nox: encaminhar argumentos de diagnóstico sem editar o noxfile.

## Fontes
- [Nox — Configuration and API](https://nox.thea.codes/en/stable/config.html) — definição de sessões, intérpretes, ambientes virtuais, tags e parâmetros; consultado em 2026-10-02.
- [Nox — Tutorial](https://nox.thea.codes/en/stable/tutorial.html) — sessões requeridas, parametrização e execução de tarefas dependentes; consultado em 2026-10-02.
