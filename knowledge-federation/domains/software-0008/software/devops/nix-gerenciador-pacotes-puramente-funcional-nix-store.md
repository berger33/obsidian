---
id: software.devops.tranche08.000781
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/NixOS/nix/master/README.md", "https://nix.dev/tutorials/first-steps/ad-hoc-shell-environments", "https://github.com/NixOS/nix"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Nix: gerenciador de pacotes puramente funcional e armazenamento imutável em /nix/store

## Em uma frase
O Nix (criado por Eelco Dolstra e licenciado sob LGPL-2.1) é um gerenciador de pacotes puramente funcional para sistemas Unix que trata pacotes como valores em linguagens funcionais puras, construindo-os a partir de funções sem efeitos colaterais e armazenando-os com hashes criptográficos em `/nix/store`.

## Por que importa
Gerenciadores de pacotes tradicionais (`apt`, `yum`, `brew`, `pip` global) sobrescrevem arquivos em diretórios compartilhados como `/usr/bin` e `/usr/lib`: atualizar uma biblioteca pode quebrar outros programas, duas versões da mesma dependência não podem coexistir facilmente e um build que funciona na máquina de um desenvolvedor falha em outra por diferenças ocultas no sistema. Segundo o README oficial do Nix (`NixOS/nix`), a abordagem puramente funcional garante que pacotes nunca mudem após serem construídos e que todas as entradas de um build sejam declaradas explicitamente.

## Como funciona
No Nix, cada pacote ou ambiente é descrito por uma expressão na linguagem Nix que avalia para uma **derivação** (`/nix/store/<hash>-<nome>.drv`). Os artefatos resultantes são gravados em diretórios imutáveis e isolados dentro de **`/nix/store/<hash>-<nome>-<versão>`**, onde `<hash>` é um hash criptográfico calculado sobre **todas** as entradas envolvidas na construção do pacote (código-fonte, script de build, compilador, flags, `glibc` e todas as dependências transitivas). Se qualquer dependência ou flag mudar, o hash muda e o pacote é instalado em um novo caminho em `/nix/store` sem sobrescrever o anterior, permitindo coexistência de múltiplas versões, atualizações atômicas e rollbacks instantâneos.

## Exemplo
```bash
# Inspecionar a versão do Nix instalada e listar entradas imutáveis endereçadas por hash em /nix/store
nix --version
ls -d /nix/store/* | head -n 5
```

## Limites e trade-offs
Como nenhuma versão antiga em `/nix/store` é sobrescrita ao atualizar pacotes ou entrar em novos ambientes de desenvolvimento (`nix-shell`), o uso de disco em `/nix/store` cresce continuamente ao longo do tempo até que o usuário ou um timer automático execute o coletor de lixo do Nix (`nix-collect-garbage -d`) para remover caminhos que não são mais referenciados por nenhum perfil ou raiz ativa (`gcroots`).

## Como verificar
Execute `nix path-info --sigs $(which nix)` (ou inspecione um caminho em `/nix/store`) para verificar o hash criptográfico e as referências exatas do pacote no Nix Store.

## Conexões
- [[nix-ambientes-efemeros-nix-shell-pacotes-isolados]] — Veja também: Nix: criação de ambientes de shell efêmeros e aninhados com nix-shell -p e execução via --run.
- [[nix-reprodutibilidade-nix-shell-pure-pinning-nixpkgs]] — Referência cruzada direta com nix-reprodutibilidade-nix-shell-pure-pinning-nixpkgs.
- [[nix-cache-binario-cache-nixos-org-derivacoes-source]] — Referência cruzada direta com nix-cache-binario-cache-nixos-org-derivacoes-source.

## Fontes
- [NixOS/nix GitHub — README.md (Purely Functional Package Manager & /nix/store Immutability)](https://raw.githubusercontent.com/NixOS/nix/master/README.md) — README oficial do Nix (LGPL-2.1) explicando o modelo puramente funcional de pacotes, hashes criptográficos de entradas em /nix/store e isolamento de dependências; consultado em 2026-10-03.
- [nix.dev Official Tutorial — Ad hoc shell environments (nix-shell, --pure, Pinning Nixpkgs & Garbage Collection)](https://nix.dev/tutorials/first-steps/ad-hoc-shell-environments) — Tutorial oficial nix.dev demonstrando criação de ambientes efêmeros e aninhados com nix-shell -p, cache binário cache.nixos.org, reprodutibilidade com --pure e -I nixpkgs=<commit> e limpeza com nix-collect-garbage; consultado em 2026-10-03.
- [NixOS/nix — Official GitHub Repository](https://github.com/NixOS/nix) — Repositório oficial do gerenciador de pacotes Nix; consultado em 2026-10-03.
