---
id: software.devops.tranche16.001509
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/carvel-dev/ytt/develop/examples/integrating-with-ytt/apis.md", "https://raw.githubusercontent.com/carvel-dev/ytt/develop/README.md", "https://carvel.dev/ytt/docs/v0.52.x/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel ytt: padrões de integração como executável externo versus módulo Go in-process

## Em uma frase
A documentação oficial de APIs do `ytt` estabelece duas estratégias para integrar o motor em ferramentas de plataforma: invocação out-of-process do binário `ytt` como executável ou importação in-process do pacote Go `carvel.dev/ytt`.

## Por que importa
Engenheiros que constroem operadores GitOps (como o `kapp-controller`), provedores Terraform (`terraform-provider-carvel`) ou CLIs internas precisam decidir entre acoplamento de biblioteca Go ou isolamento de processo.

## Como funciona
Para a maioria dos casos, a equipe Carvel recomenda a integração como executável externo, pois desacopla o ciclo de atualização do `ytt` da ferramenta hospedeira, preserva todas as verificações de entrada da CLI e executa bibliotecas complexas em menos de um segundo. A integração como módulo Go (`template.NewOptions()` e `opts.RunWithFiles(inputs, ui)`) é indicada quando a distribuição em binário único estático é obrigatória, ciente de que as interfaces Go internas podem mudar entre versões.

## Exemplo
```bash
ytt -f config/ --output-files /tmp/rendered-manifests
ls -la /tmp/rendered-manifests
```

## Limites e trade-offs
Ao importar `carvel.dev/ytt` diretamente no `go.mod`, o projeto assume o custo de adaptar chamadas internas em bumps de versão, já que o Carvel garante compatibilidade retroativa para o comportamento da CLI, mas não congela as assinaturas Go internas.

## Como verificar
Teste o pipeline de renderização invocando `ytt -f config/ --output-files out/` e valide o código de retorno `0` e os arquivos YAML gerados no diretório de destino.

## Conexões
- [[carvel-ytt-precedencia-valores-data-values-file-env-flags]] — Veja também: Carvel ytt: ordem de precedência e injeção de Data Values via arquivos, variáveis de ambiente e flags CLI.
- [[carvel-ytt-pos-processamento-helm-template-kustomize-pipeline]] — Veja também: Carvel ytt: pós-processamento seguro de gráficos Helm de terceiros sem fork de templates.

## Fontes
- [Carvel ytt GitHub — README.md (Structural YAML Templating, Starlark, Custom Validations, Overlays & Sandboxing)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/examples/integrating-with-ytt/apis.md) — README oficial do carvel-dev/ytt detalhando templating estrutural ciente de YAML, linguagem Starlark determinística, overlays e validações; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — About ytt v0.52.x (Templating, Data Values, Patching/Overlaying & Modularizing)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/README.md) — Documentação oficial do Carvel ytt explicando anotações #@, Data Values, módulo @ytt:overlay, fragmentos YAML e bibliotecas _ytt_lib; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — Application Programming Interfaces of ytt (Executable vs Go Module Integration)](https://carvel.dev/ytt/docs/v0.52.x/) — Guia oficial de integração do Carvel ytt comparando invocação como executável externo versus módulo Go in-process; consultado em 2026-10-03.
