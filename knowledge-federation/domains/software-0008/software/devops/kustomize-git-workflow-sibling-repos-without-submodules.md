---
id: software.devops.tranche01.000067
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md", "https://kubectl.docs.kubernetes.io/references/kustomize/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fluxo Git com repositórios irmãos em disco: consumindo bases upstream sem precisar de Git submodules

## Em uma frase
Dois parágrafos estratégicos nos passos 1 e 2 da seção Usage do README explicam como o modelo do Kustomize facilita o controle de versão com `git`: a pasta `base` pode conter arquivos de um repositório upstream mantido por outra equipe ou projeto aberto, enquanto os `overlays` ficam em um repositório próprio da sua organização; posicionar os clones dos repositórios como diretórios irmãos no disco evita a necessidade de usar `git submodules` (embora submódulos também funcionem para quem preferir).

## Por que importa
Quando uma equipe customiza manifestos oficiais de um projeto open-source editando os arquivos diretamente, atualizar para a próxima versão upstream gera conflitos manuais em dezenas de YAMLs; manter a base intocada num clone irmão (ou branch limpa) e manter apenas os overlays no seu próprio repositório separa completamente o ciclo de vida upstream das customizações locais.

## Como funciona
Se a base vier de um repositório externo, mantenha seus arquivos originais sem edição direta e organize seus overlays em um diretório irmão no sistema de arquivos apontando o caminho relativo para a base, simplificando rebases e atualizações sem exigir `git submodules`.

## Exemplo
Como o Kustomize nunca altera os arquivos dentro da base durante o `kustomize build`, um simples `git pull` ou `git rebase` na base captura as melhorias do autor original imediatamente.

## Limites e trade-offs
Ao usar diretórios irmãos provenientes de dois repositórios Git distintos no pipeline de CI/CD, garanta que o job faça checkout de ambos os repositórios nas pastas relativas esperadas pelo `kustomization.yaml` do overlay.

## Como verificar
Conferi os comentários sobre `git`, rebase de forks e clones irmãos sem `git submodules` nos passos 1 e 2 de Usage no README oficial.

## Conexões
- [[kustomize-patches-replica-and-cpu-count-example]] — Veja também: Aplicação declarativa de `patches` em overlays: ajustando réplicas e limites de CPU por ambiente.
- [[kustomize-labels-with-include-selectors]] — Veja também: Propagação de rótulos com `labels:` e o efeito de `includeSelectors: true` na base e no overlay.

## Fontes
- [Kustomize — README oficial](https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md) — README oficial do Kustomize com customização YAML template-free (analogia make/sed), matriz de versões embutidas no kubectl, kustomization.yaml com labels/includeSelectors/configMapGenerator, kustomize build e overlays com patches.; consultado em 2026-10-03.
- [Kustomize — documentação oficial de referência](https://kubectl.docs.kubernetes.io/references/kustomize/) — Documentação oficial de referência e glossário do Kustomize mantida pelo sig-cli do Kubernetes.; consultado em 2026-10-03.
