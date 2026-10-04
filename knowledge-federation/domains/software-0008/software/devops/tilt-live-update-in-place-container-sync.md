---
id: software.devops.tranche06.000522
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/tilt-dev/tilt/master/README.md", "https://docs.tilt.dev/tutorial/index.html", "https://github.com/tilt-dev/tilt"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Atualizações instantâneas sem rebuild de imagem com o recurso Live Update do Tilt

## Em uma frase
A seção *5. Smart Rebuilds with Live Update* do tutorial oficial (`docs.tilt.dev/tutorial/index.html`) destaca um dos recursos mais poderosos do Tilt para produtividade de desenvolvimento: o **Live Update**. Em vez de reconstruir uma imagem OCI inteira do zero, enviá-la ao registro e recriar o Pod no Kubernetes a cada linha de código editada, o Live Update sincroniza os arquivos alterados diretamente para dentro do contêiner já em execução e pode executar comandos leves de atualização in-place (como recompilar incrementalmente ou reiniciar o processo interno), oferecendo feedback de sub-segundo mesmo para linguagens e frameworks que não possuem hot reload nativo.

## Por que importa
Um ciclo completo de `docker build` + `docker push` + `Pod recreate` + inicialização do contêiner facilmente leva de 30 segundos a 2 minutos; reduzir esse ciclo para 1 ou 2 segundos com Live Update preserva o estado de fluxo (*flow state*) do desenvolvedor.

## Como funciona
Configure regras de `live_update` (como `sync(...)`, `run(...)` e `fall_back_on(...)`) na função `docker_build` do seu `Tiltfile`, seguindo os guias oficiais de boas práticas do README para **HTML, Node.js, Python, Go, Java e C#**.

## Exemplo
Em um serviço Go ou Python rodando no cluster local via Tilt, o desenvolvedor altera um handler HTTP e salva o arquivo; o Live Update copia a alteração para o contêiner em execução e atualiza o processo em menos de 2 segundos sem recriar o Pod no Kubernetes.

## Limites e trade-offs
Utilize sempre a diretiva `fall_back_on(['package.json', 'go.mod', 'Dockerfile'])` dentro do `live_update` para forçar um rebuild limpo de imagem completa sempre que arquivos estruturais de dependências forem alterados.

## Como verificar
Edite um arquivo coberto por `live_update` com o `tilt up` ativo e verifique no painel do Tilt que a atualização ocorreu via sincronização ao vivo sem troca do nome do Pod.

## Conexões
- [[tilt-kubernetes-for-prod-tilt-for-dev-control-loop]] — Veja também: O loop de controle do Tilt (tilt up): automação contínua entre alteração de código e atualização no Kubernetes.
- [[tilt-tilt-ui-aggregated-logs-and-resource-status]] — Veja também: Visibilidade centralizada e agregação de logs multi-serviço na interface Tilt UI.

## Fontes
- [Tilt GitHub — README.md (Kubernetes for Prod, Tilt for Dev, tilt up, Tiltfile API, Extensions & Security)](https://raw.githubusercontent.com/tilt-dev/tilt/master/README.md) — README oficial do Tilt (Apache-2.0) detalhando o lema Kubernetes for Prod, Tilt for Dev, o comando tilt up para automação de observação de arquivos, build de imagens e atualização do ambiente, guias por linguagem (HTML, NodeJS, Python, Go, Java, C#), referência da API do Tiltfile, repositório tilt-extensions, telemetria anônima e reporte privado de segurança para security@docker.com.; consultado em 2026-10-03.
- [Tilt Official Documentation — First Look at Tilt Tutorial (Control Loop, Tilt UI, Smart Rebuilds & Live Update)](https://docs.tilt.dev/tutorial/index.html) — Tutorial oficial de introdução ao Tilt detalhando o loop de controle do tilt up, a interface agregadora Tilt UI, rebuilds inteligentes e o mecanismo de Live Update para sincronização instantânea de alterações em contêineres sem rebuild completo.; consultado em 2026-10-03.
- [Tilt — Official GitHub Repository](https://github.com/tilt-dev/tilt) — Repositório oficial Apache-2.0 do Tilt.; consultado em 2026-10-03.
